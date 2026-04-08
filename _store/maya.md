---
aid: maya
url: https://raw.githubusercontent.com/api-evangelist/maya/refs/heads/main/apis.yml
apis:
- name: Maya Python API 2.0
  description: Modern Python API for Maya scripting and plugin development, offering improved performance and a more Pythonic interface compared to API 1.0.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2026/ENU/
  baseUrl: https://localhost
  tags:
  - Automation
  - OpenMaya
  - Plugins
  - Python
  - Scripting
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Maya_Python_API_2_0_html
  - type: X-api-reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_py_ref_index_html
  - type: X-python-api-2-reference-2026
    url: https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/py_ref/namespace_open_maya.html
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
    X-twitter: autodesk
- name: Maya Python API 1.0
  description: Original Python wrapper for the Maya C++ API providing access to OpenMaya, OpenMayaUI, OpenMayaAnim, OpenMayaFX, OpenMayaRender, and OpenMayaCloth modules.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Maya_Python_API_1_0_html
  baseUrl: https://localhost
  tags:
  - OpenMaya
  - Plugins
  - Python
  - Scripting
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Maya_Python_API_1_0_html
  - type: X-modules
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_Maya_Python_API_1_0_Modules_html
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
    X-twitter: autodesk
- name: Maya C++ API
  description: C++ API for high-performance Maya plugin development, providing low-level access to Maya internals through OpenMaya, OpenMayaUI, OpenMayaAnim, OpenMayaFX, and OpenMayaRender libraries.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2024/ENU/
  baseUrl: https://localhost
  tags:
  - C++
  - OpenMaya
  - Performance
  - Plugins
  - SDK
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_SDK_html
  - type: X-api-reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_cpp_ref_index_html
  - type: X-getting-started
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_API_introduction_API_Basics_html
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Maya Commands (MEL)
  description: Maya Embedded Language command API for scripting and automating tasks within Maya using the built-in MEL interpreter.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2024/ENU/
  baseUrl: https://localhost
  tags:
  - Automation
  - Commands
  - MEL
  - Scripting
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html
  - type: X-api-reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__Commands_index_html
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Maya Commands (Python)
  description: Python command interface (maya.cmds) providing access to all MEL commands through Python, enabling scripting and automation with Python syntax.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2025/ENU/?guid=GUID-55B63946-CDC9-42E5-9B6E-45EE45CFC7FC
  baseUrl: https://localhost
  tags:
  - Automation
  - Commands
  - Python
  - Scripting
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2025/ENU/?guid=GUID-55B63946-CDC9-42E5-9B6E-45EE45CFC7FC
  - type: X-api-reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Maya USD API
  description: Universal Scene Description integration API for Maya, enabling USD stage loading, editing, and interchange within the Maya viewport.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2024/ENU/
  baseUrl: https://localhost
  tags:
  - Interchange
  - OpenUSD
  - Pipeline
  - Pixar
  - USD
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Merged_USD_SDK_html
  - type: X-getting-started
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-02B222AB-0D49-4D41-B785-E1F5EECF7DF9
  - type: X-github
    url: https://github.com/Autodesk/maya-usd
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Maya Batch Rendering API
  description: API for batch rendering and render farm integration, enabling automated rendering workflows and pipeline integration.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://help.autodesk.com/view/MAYAUL/2024/ENU/
  baseUrl: https://localhost
  tags:
  - Batch
  - Pipeline
  - Rendering
  properties:
  - type: X-documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-C99B0FD5-BE5F-4AC1-BA3B-566485FE5EE3
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Maya Hydra API
  description: Maya plugin API that replaces the main Maya viewport with a Hydra viewer, enabling custom render delegate integration for viewport rendering.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://github.com/Autodesk/maya-hydra
  baseUrl: https://localhost
  tags:
  - Hydra
  - OpenSource
  - Rendering
  - Viewport
  properties:
  - type: X-github
    url: https://github.com/Autodesk/maya-hydra
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
- name: Autodesk Platform Services - Maya API
  description: Cloud-based API for Maya through Autodesk Platform Services (APS), providing web service integration, OAuth authentication, and cloud workflow capabilities for Maya development.
  image: https://www.autodesk.com/products/maya/overview
  humanUrl: https://aps.autodesk.com/developer/overview/maya
  baseUrl: https://aps.autodesk.com
  tags:
  - APS
  - Cloud
  - OAuth
  - Platform
  - REST
  properties:
  - type: X-documentation
    url: https://aps.autodesk.com/developer/overview/maya
  - type: X-authentication
    url: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/basics
  - type: X-api-reference
    url: https://aps.autodesk.com/developer/documentation
  - type: X-getting-started
    url: https://tutorials.autodesk.io/
  contact:
  - FN: Autodesk Support
    email: maya.support@autodesk.com
name: Maya
tags:
- 3D
- Animation
- Autodesk
- CGI
- Modeling
- Rendering
- Scripting
- VFX
type: Contract
image: https://www.autodesk.com/products/maya/overview
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for Maya, the popular 3D animation and modeling software developed by Autodesk, providing scripting and plugin development capabilities through Python, C++, MEL, and .NET interfaces.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

