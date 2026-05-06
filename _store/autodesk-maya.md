---
aid: autodesk-maya
name: Autodesk Maya
description: Autodesk Maya is a comprehensive 3D computer graphics application used for creating interactive 3D applications including video games, animated films, TV series, and visual effects. Maya provides multiple programming APIs including a Python API, C++ plugin API, MEL scripting language, USD integration, and Bifrost visual programming environment for extending and automating Maya workflows and creating custom tools and plugins.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 3D Graphics
  - Animation
  - Game Development
  - Modeling
  - Rendering
  - Visual Effects
  - VFX
  - CAD
url: https://raw.githubusercontent.com/api-evangelist/autodesk-maya/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autodesk-maya:maya-python-api
    name: Maya Python API
    description: Python API for scripting and extending Maya functionality, providing access to Maya's scene graph and node architecture. Includes Python API 2.0 with a more Pythonic workflow and improved performance via maya.api.OpenMaya, as well as Python API 1.0 via maya.OpenMaya and the maya.cmds wrapper for MEL commands.
    humanURL: https://help.autodesk.com/view/MAYAUL/2026/ENU/
    baseURL: https://localhost
    tags:
      - Automation
      - Python
      - Scripting
    properties:
      - type: Documentation
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_Python_API_Maya_Python_API_2_0_html
      - type: APIReference
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_py_ref_index_html
      - type: GettingStarted
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_Python_API_Python_API_2_0_Quick_Start_html
  - aid: autodesk-maya:maya-cpp-api
    name: Maya C++ API
    description: C++ API providing low-level access to Maya's core functionality for creating plugins, custom nodes, and high-performance tools. The API is organized into functional libraries including OpenMaya, OpenMayaUI, OpenMayaAnim, OpenMayaFX, and OpenMayaRender.
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
      - type: APIReference
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_cpp_ref_index_html
      - type: GettingStarted
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_MERGED_Maya_SDK_Maya_SDK_html
  - aid: autodesk-maya:maya-mel-commands
    name: Maya Commands (MEL)
    description: Maya Embedded Language (MEL) scripting interface for automating tasks and customizing Maya workflows. MEL provides direct access to Maya commands and is the foundation of Maya's scripting capabilities.
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
      - type: APIReference
        url: https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__Commands_index_html
  - aid: autodesk-maya:maya-usd-api
    name: Maya USD API
    description: Universal Scene Description (USD) integration for Maya, enabling exchange of 3D content between applications. Provides tools for importing, exporting, and working with USD stages and layers within Maya.
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
      - type: GitHubRepository
        url: https://github.com/Autodesk/maya-usd
  - aid: autodesk-maya:maya-bifrost-api
    name: Maya Bifrost API
    description: Bifrost is Maya's visual programming environment for creating simulation and procedural effects. It provides a node-based graph editor for building complex effects including fluids, particles, destruction, and procedural geometry, with SDK support for custom node development.
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
      - type: GitHubRepository
        url: https://github.com/Autodesk/bifrost-usd
common:
  - type: Portal
    url: https://www.autodesk.com/developer-network/platform-technologies/maya
  - type: Documentation
    url: https://help.autodesk.com/view/MAYADEV/2026/ENU/
  - type: Support
    url: https://forums.autodesk.com/t5/maya-programming/bd-p/area-c-maya-programming
  - type: Blog
    url: https://www.autodesk.com/blogs/maya/
  - type: Tutorials
    url: https://tutorials.autodesk.io/
  - type: ReleaseNotes
    url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=MAYA_RELEASENOTES_2026_RELEASE_NOTES_HTML
  - type: TermsOfService
    url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services
  - type: GitHubOrganization
    url: https://github.com/autodesk-platform-services
  - type: Features
    data:
      - name: Python API 2.0
        description: Modern Pythonic API with improved performance and a cleaner interface for accessing Maya's node architecture and scene graph via maya.api.OpenMaya.
      - name: C++ Plugin SDK
        description: Low-level C++ API for high-performance plugin development with access to Maya's full internal architecture through OpenMaya functional libraries.
      - name: MEL Scripting
        description: Maya Embedded Language for command-line scripting, UI automation, and batch processing of Maya scenes and assets.
      - name: USD Integration
        description: Universal Scene Description support for importing, exporting, and working with USD assets within Maya for cross-application 3D content pipelines.
      - name: Bifrost Visual Programming
        description: Node-based visual programming environment for creating procedural effects, simulations, and custom workflows without traditional coding.
      - name: Custom Node Development
        description: Create custom dependency graph nodes, deformers, and shape nodes that integrate natively into Maya's scene graph and evaluation system.
  - type: UseCases
    data:
      - name: VFX Pipeline Integration
        description: Integrating Maya into visual effects production pipelines with custom tools, asset management systems, and render farm automation.
      - name: Game Asset Automation
        description: Automating game asset creation, optimization, and export workflows for game engines like Unreal Engine and Unity through Maya scripting.
      - name: Animation Workflow Tools
        description: Building custom rigging systems, animation controls, and workflow tools to accelerate character animation production for film and TV.
      - name: Procedural Content Generation
        description: Using Bifrost and Python APIs to generate procedural geometry, textures, and scene content for games, visualization, and architectural projects.
      - name: DCC Pipeline Development
        description: Developing studio pipeline tools that automate scene assembly, asset tracking, and data interchange between Maya and other DCC applications.
  - type: Integrations
    data:
      - name: Autodesk Arnold
        description: Integration with Arnold renderer via the MtoA (Maya to Arnold) plugin for photorealistic rendering of Maya scenes.
      - name: Unreal Engine
        description: USD-based pipeline integration with Unreal Engine for game asset export and visualization workflows.
      - name: ShotGrid (Flow Production Tracking)
        description: Integration with Autodesk ShotGrid for production tracking, asset management, and review workflows in film and TV production.
      - name: Houdini
        description: Interoperability with SideFX Houdini via USD and Alembic for visual effects simulation and procedural content pipelines.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
