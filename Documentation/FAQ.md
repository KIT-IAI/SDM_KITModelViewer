# FAQ

## Why is the coordinate system unknown?

Since there are numerous EPSG codes, only the most common SRS systems have been implemented. Additional systems will be added upon request. If your data uses a CRS that is not yet supported, please contact us or create an issue, specifying the corresponding EPSG code and, if possible, attaching a sample data set.

If an unknown SRS is displayed after import, the corresponding dataset can still be imported. To avoid problems with large coordinate values, we recommend switching to “Local CRS (reduced coordinates)” in this case.

> [!NOTE]
> When using a local CRS, it is not possible to display the data in a geographic context (e.g., by overlaying it on a map).

## Why is the scene empty after loading a file?

This issue can occur when the coordinate system is activated and the data contains very large coordinates. If the distance from the coordinate origin is too large, the entire scene may be displayed at such a small scale that it appears as a blank white screen.

Solution: Try deactivating the coordinate system by clicking the small tripod icon in the toolbar.

## What should I select when opening a ZIP file?

When you open a ZIP file, a dialog box displays the contents of the archive. Only supported file types are shown automatically.

Selected files are loaded into separate new documents unless the option to merge them into a single scene is enabled.

> [!NOTE]
> Do not select any texture files. Textures are reloaded automatically.
