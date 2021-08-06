# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# Name: NF Water Buffer Maker
# Purpose: Combines all inputted polygon and line .shp files and adds buffer "x" and calculates area
#
# Author: Elijah Nicpon, (the coolest 2021 Summer Intern ever)
# Copyright: (c) enicpon3 2021
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# INITIALIZATION
# --------------------------------------------------------------------------------------------------------------------

import os, arcpy

arcpy.env.overwriteOutput = True
outpath = arcpy.GetParameterAsText(0)
gbd_name = "Water_Buffer_Tool"
tempdata = os.path.join(outpath, gbd_name)
cursor_field_names = ["FID", "Shape"]


# --------------------------------------------------------------------------------------------------------------------

def new_shp_file(file_short_name):
    try:
        os.remove(os.join(outpath, file_short_name))
    except:
        doNothing = True
    arcpy.management.CreateFeatureclass(outpath, file_short_name, geometry_type="MULTIPOINT", spatial_reference=spatial_ref)
    location = os.path.join(outpath, file_short_name)
    return location


def merge_shps(shp, target_location):
    arcpy.Merge_management(shp, target_location)


def bufferer(shp, target_location):
    arcpy.Buffer_analysis(shp, target_location, linear_unit, dissolve_option="ALL")


def clipper(input, clip_feature, output):
    arcpy.analysis.Clip(input, clip_feature, output)


def area_calc(input, output):
    total_area = 0.0
    arcpy.CalculateAreas_stats(input, output)
    arcpy.AddMessage("Area field \"F_AREA\" has been added and calculated in the file " + output)
    try:
        with arcpy.da.SearchCursor(output, "F_AREA") as cursor:  # -
            for x in cursor:
                total_area += x[0]
    except:
        total_area = "Failed"
    return str(total_area)


# --------------------------------------------------------------------------------------------------------------------

input_shps = arcpy.GetParameterAsText(1)
input_shps = input_shps.replace("\'", "")
input_shps = input_shps.split(";")
boundary = arcpy.GetParameterAsText(2)
boundary_FID = arcpy.GetParameterAsText(3)
if boundary != "":
    if boundary_FID != "":
        try:
            with arcpy.da.SearchCursor(boundary, cursor_field_names) as boundary_cursor:  # -
                for x in boundary_cursor:  # - IS THIS FASTEST?
                    if x[0] == boundary_FID:
                        boundary = x
                        break
        except:
            arcpy.AddMessage(
                "Failed to locate FID " + boundary_FID + " in " + boundary + ". Continuing without clipping to a boundary")
            boundary = ""
else:
    arcpy.AddMessage("Warning: Boundary field left empty. Process will continue.")
linear_unit = arcpy.GetParameterAsText(4)
sr_temp = arcpy.GetParameterAsText(5)  # Optional: can be file location, exact text, or SR code
if sr_temp != "":
    try:
        try:
            spatial_ref = arcpy.SpatialReference(sr_temp)
        except:
            spatial_ref = sr_temp
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(spatial_ref)
        arcpy.AddMessage("Spatial reference successfully set to desired value.")
    except:
        spatial_ref = arcpy.Describe(input_shps[0]).spatialReference
        arcpy.AddMessage("Failed to find your requested spatial reference. Matching spatial reference to input.")
else:
    spatial_ref = arcpy.Describe(input_shps[0]).spatialReference
    arcpy.AddMessage("Matching spatial reference to input.")

arcpy.AddMessage("File output location is " + outpath + "\n")

# --------------------------------------------------------------------------------------------------------------------
# Step 0: Create necessary files
combined = new_shp_file("combined.shp")
temp_combined_clip1 = new_shp_file("temp_combined_clip1.shp")
temp_combined_buffered = new_shp_file("temp_combined_buffered.shp")
combined_clipped_buffered = new_shp_file("combined_clipped_buffered.shp")
combined_final = new_shp_file("combined_final.shp")

polygons = new_shp_file("polygons.shp")
temp_polygons_clip1 = new_shp_file("temp_polygons_clip1.shp")
polygons_clipped = new_shp_file("polygons_clipped.shp")
polygons_final = new_shp_file("polygons_final.shp")

temp_boundary_buffered = new_shp_file("temp_boundary_buffered.shp")
# --------------------------------------------------------------------------------------------------------------------
# Part 1: Convert Rasters and Merge Files and Duplicate polygons only
for y in input_shps:
    arcpy.AddMessage("Reading " + y)
    if y[(y.rfind(".")):(len(y))] != ".shp":
        arcpy.AddMessage("Attempting to convert " + y)
        try:
            newfilename = y.replace(".", "") + "_converted.shp"
            arcpy.RasterToPolygon_conversion(y, newfilename)
            input_shps.append(newfilename)
        except:
            arcpy.AddMessage("File " + y + " is not a .shp file and cannot be converted. It will be skipped.")
        input_shps.remove(y)
    arcpy.AddMessage("Merging files.")
for y in input_shps:
    merge_shps(y, combined)
arcpy.AddMessage("Combined all .shp files into " + combined + ".\n")

with arcpy.da.SearchCursor(combined, cursor_field_names) as cursor:
    for row in cursor:
        if (row[1] == "Polygon"):
            merge_shps(x, polygons)
    arcpy.AddMessage("Combined all wetland .shp files that are polygons into " +
                     polygons + "\n")

# --------------------------------------------------------------------------------------------------------------------
# Part 2: Mini clip (clip to buffered boundary for speed) and buffer
if boundary != "":
    bufferer(boundary, temp_boundary_buffered)
    clipper(combined, temp_boundary_buffered, temp_combined_clip1)
    clipper(polygons, temp_boundary_buffered, temp_polygons_clip1)
    bufferer(temp_combined_clip1, temp_combined_buffered)
    # bufferer(temp_polygons_clip1, temp_polygons_buffered)
# --------------------------------------------------------------------------------------------------------------------
# Part 3: Actually clip to boundary
    clipper(temp_combined_buffered, boundary, combined_clipped_buffered)
    clipper(temp_polygons_clip1, boundary, polygons_clipped)
# --------------------------------------------------------------------------------------------------------------------
# Part 3: Calculate Area
combined_area = area_calc(combined_clipped_buffered, combined_final)
try:
    polygon_area = area_calc(polygons_clipped, polygons_final)
except:
    arcpy.AddMessage("polygons failed")

arcpy.AddMessage("The buffered area is " + combined_area + str(linear_unit))
try:
    arcpy.AddMessage("The area without buffers is " + polygon_area)
except:
    arcpy.AddMessage("polygons failed")

temp_files = [temp_combined_clip1, temp_combined_buffered, temp_polygons_clip1, temp_boundary_buffered,
              combined_clipped_buffered, polygons_clipped]
sep = "; "
arcpy.AddMessage("Removing following temp files: " + sep.join(temp_files))
for x in temp_files:
    os.remove(x)

arcpy.AddMessage("Script finished. Your buffered, clipped, and combined shape file is here: " + combined_final)
arcpy.AddMessage(
    "The shape file with the polygons only, (used to calculate area without buffers), clipped to the boundary, is located here: " + polygons_final)
