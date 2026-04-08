---
aid: autodesk-maya
url: https://raw.githubusercontent.com/api-evangelist/autodesk-maya/refs/heads/main/apis.yml
apis:
- name: Maya Python API
  description: Python API for scripting and extending Maya functionality, providing access to Maya's scene graph and node architecture. Includes Python API 2.0 with a more Pythonic workflow and improved performance via maya.api.OpenMaya, as well as Python API 1.0 via maya.OpenMaya and the maya.cmds wrapper for MEL commands.
  image: https://www.autodesk.com/products/maya/overview
  humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/
  baseURL: https://localhost
  tags:
  - Automation
  - Python
  - Scripting
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_Python_API_Maya_Python_API_2_0_html
  - type: API Reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_py_ref_index_html
  - type: Getting Started
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_Python_API_Python_API_2_0_Quick_Start_html
  - type: Python API 2.0 Reference (2026)
    url: https://help.autodesk.com/cloudhelp/2026/CHS/MAYA-API-REF/py_ref/
  - type: Python Commands Reference
    url: https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/about.html
  - type: Python in Maya Guide
    url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=GUID-C0F27A50-3DD6-454C-A4D1-9E3C44B3C990
  - type: Using Python
    url: https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Scripting/files/GUID-55B63946-CDC9-42E5-9B6E-45EE45CFC7FC.htm
- name: Maya C++ API
  description: C++ API providing low-level access to Maya's core functionality for creating plugins, custom nodes, and high-performance tools. The API is organized into functional libraries including OpenMaya, OpenMayaUI, OpenMayaAnim, OpenMayaFX, and OpenMayaRender.
  image: https://www.autodesk.com/products/maya/overview
  humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/
  baseURL: https://localhost
  tags:
  - C++
  - Native
  - Performance
  - Plugins
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_cpp_ref_index_html
  - type: API Reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_cpp_ref_index_html
  - type: Developer Guide
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_SDK_Maya_SDK_html
  - type: C++ API Reference (2026)
    url: https://help.autodesk.com/cloudhelp/2026/JPN/MAYA-API-REF/cpp_ref/
  - type: What's New in 2026 DevKit
    url: https://help.autodesk.com/view/MAYADEV/2026/ENU/?guid=2026-Whats-New-in-API
- name: Maya Commands (MEL)
  description: Maya Embedded Language (MEL) scripting interface for automating tasks and customizing Maya workflows. MEL provides direct access to Maya commands and is the foundation of Maya's scripting capabilities.
  image: https://www.autodesk.com/products/maya/overview
  humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/
  baseURL: https://localhost
  tags:
  - Automation
  - Commands
  - MEL
  - Scripting
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html
  - type: Command Reference
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__Commands_index_html
  - type: MEL Guide
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__files_GUID_58E4E64B_79C4_46E3_B0A7_CD7D2BFD3BFF_htm
  - type: MEL Command Syntax (2026)
    url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=GUID-579A6D9F-CB41-4CD9-B9D7-3DB1FD33735D
- name: Maya USD API
  description: Universal Scene Description (USD) integration for Maya, enabling exchange of 3D content between applications. Provides tools for importing, exporting, and working with USD stages and layers within Maya.
  image: https://www.autodesk.com/products/maya/overview
  humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/
  baseURL: https://localhost
  tags:
  - Interchange
  - Pipeline
  - Scene Description
  - USD
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-C7DB6AF9-653E-4B49-93D6-F9C2D0865B85
  - type: GitHub Repository
    url: https://github.com/Autodesk/maya-usd
- name: Maya Bifrost API
  description: Bifrost is Maya's visual programming environment for creating simulation and procedural effects. It provides a node-based graph editor for building complex effects including fluids, particles, destruction, and procedural geometry, with SDK support for custom node development.
  image: https://www.autodesk.com/products/maya/overview
  humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=GUID-1223AA4F-1CD7-473C-87EA-C16C6B28F7FD
  baseURL: https://localhost
  tags:
  - Bifrost
  - Particles
  - Procedural Effects
  - Simulation
  - Visual Programming
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=Bifrost_MayaPlugin_bifrost_for_maya_html
  - type: Bifrost Help
    url: https://help.autodesk.com/view/BIFROST/ENU/
  - type: Node Reference
    url: https://help.autodesk.com/view/BIFROST/ENU/?guid=Bifrost_Common_reference_html
  - type: GitHub Repository (Bifrost USD)
    url: https://github.com/Autodesk/bifrost-usd
  - type: What's New in Bifrost 2.13 (Maya 2026)
    url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=GUID-EA529440-E7A6-48E6-B215-691CDD34320A
name: Autodesk Maya
tags:
- 3D Graphics
- Animation
- Game Development
- Modeling
- Rendering
- Visual Effects
type: Contract
image: https://www.autodesk.com/products/maya/overview
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and SDKs for Autodesk Maya, a comprehensive 3D computer graphics application used for creating interactive 3D applications including video games, animated films, TV series, and visual effects.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

