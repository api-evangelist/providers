---
aid: blender
name: Blender
description: Blender is the free and open source 3D creation suite supporting the entirety of the 3D pipeline including modeling, rigging, animation, simulation, rendering, compositing, motion tracking, video editing, and game creation. Blender's Python API provides extensive scripting capabilities for automation, tool development, and addon creation, enabling developers to extend Blender with custom functionality. The project is governed by the Blender Foundation and maintained at blender.org.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 3D
  - Animation
  - Game Development
  - Modeling
  - Open Source
  - Python
  - Rendering
  - VFX
url: https://raw.githubusercontent.com/api-evangelist/blender/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: blender:blender-python-api
    name: Blender Python API
    description: The Blender Python API (bpy) provides Python access to Blender's internal data, operators, and UI components. It enables developers to automate tasks, create addons, build custom tools, manipulate scene data, interact with the render pipeline, and extend Blender's interface. The API is embedded within Blender and does not expose HTTP endpoints; it is invoked via Blender's built-in Python interpreter or through command-line batch rendering.
    humanURL: https://docs.blender.org/api/current/
    tags:
      - Addons
      - Automation
      - Open Source
      - Python
      - Scripting
    properties:
      - type: Documentation
        url: https://docs.blender.org/api/current/
      - type: GitHub
        url: https://github.com/blender/blender
      - type: GettingStarted
        url: https://docs.blender.org/api/current/info_quickstart.html
      - type: Tutorials
        url: https://docs.blender.org/api/current/info_tips_and_tricks.html
      - type: JSONSchema
        url: json-schema/blender-addon-manifest-schema.json
      - type: JSONSchema
        url: json-schema/blender-bpy-operator-schema.json
      - type: JSONStructure
        url: json-structure/blender-addon-manifest-structure.json
      - type: JSONStructure
        url: json-structure/blender-bpy-operator-structure.json
      - type: JSONLD
        url: json-ld/blender-context.jsonld
      - type: Example
        url: examples/blender-addon-manifest-example.json
      - type: Example
        url: examples/blender-bpy-operator-example.json
  - aid: blender:blender-extensions
    name: Blender Extensions Platform
    description: The Blender Extensions Platform (extensions.blender.org) provides a curated repository of addons, themes, and node presets for Blender. The platform supports structured addon packaging, versioning, and distribution. Developers can publish addons with metadata via the extensions.blender.org manifest format.
    humanURL: https://extensions.blender.org
    tags:
      - Addons
      - Extensions
      - Marketplace
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.blender.org/manual/en/latest/extensions/index.html
      - type: Portal
        url: https://extensions.blender.org
common:
  - type: Website
    url: https://www.blender.org/
  - type: Documentation
    url: https://docs.blender.org/
  - type: GettingStarted
    url: https://docs.blender.org/api/current/info_quickstart.html
  - type: Community
    url: https://www.blender.org/community/
  - type: Support
    url: https://www.blender.org/support/
  - type: GitHubOrganization
    url: https://github.com/blender
  - type: GitHub
    url: https://github.com/blender/blender
  - type: Blog
    url: https://www.blender.org/news/
  - type: Training
    url: https://www.blender.org/training/
  - type: FAQ
    url: https://www.blender.org/support/faq/
  - type: ReleaseNotes
    url: https://developer.blender.org/docs/release_notes/
  - type: License
    url: https://www.blender.org/about/license/
    title: GPL-2.0-or-later
  - type: PackageRegistry
    url: https://extensions.blender.org
  - type: SpectralRules
    url: rules/blender-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/blender-python-api.yaml
  - type: Vocabulary
    url: vocabulary/blender-vocabulary.yaml
  - type: Features
    data:
      - name: Python Scripting (bpy)
        description: The bpy module provides access to Blender's internal data model, allowing Python scripts to create, read, update, and delete scene objects, materials, animations, constraints, and render settings.
      - name: Operator Framework
        description: Blender's operator system allows Python developers to create custom operators (commands) accessible from menus, panels, keyboard shortcuts, and scripts.
      - name: Addon Development
        description: Blender addons are Python packages extending functionality across modeling, rigging, animation, rendering, import/export, and UI. Distributed via the Extensions Platform or bundled directly.
      - name: Node Groups and Geometry Nodes
        description: Geometry Nodes and Shader Nodes provide visual programming for procedural modeling and materials, scriptable via the Python API.
      - name: Render Pipeline Integration
        description: Python API integrates with Blender's Cycles and EEVEE render engines for batch rendering, render farm integration, and custom render pipeline control.
      - name: Command-Line Interface
        description: Blender can be invoked headlessly via CLI for batch rendering, script execution, and pipeline automation without a GUI.
      - name: Asset Library System
        description: Blender 3.x+ includes an asset library system with Python API support for managing and accessing reusable 3D assets across projects.
  - type: UseCases
    data:
      - name: Pipeline Automation
        description: VFX and animation studios automate Blender production pipelines using Python scripts for batch rendering, asset processing, and scene assembly.
      - name: Addon Development
        description: Developers create custom tools and plugins extending Blender's functionality for modeling, rigging, simulation, and export workflows.
      - name: Headless Rendering
        description: Blender is used for headless server-side rendering via CLI and Python scripts in cloud rendering pipelines and automated content generation workflows.
      - name: Procedural Content Generation
        description: Python scripts and Geometry Nodes enable procedural generation of 3D assets for games, VFX, and architectural visualization.
      - name: Education and Research
        description: Universities, research labs, and educators use Blender's Python API for 3D visualization, scientific rendering, and computer graphics research.
  - type: Integrations
    data:
      - name: Cycles X Render Engine
        description: Blender's built-in path-tracing render engine with Python API access for controlling render settings, passes, and denoising.
      - name: USD (Universal Scene Description)
        description: Blender supports import and export of Pixar USD scenes, enabling pipeline integration with VFX and game development workflows.
      - name: glTF 2.0
        description: Blender has built-in glTF 2.0 import/export support with Python API access, enabling web, AR/VR, and game engine pipelines.
      - name: OpenVDB
        description: Blender supports OpenVDB for volumetric simulation and rendering, with Python API access to volume data and simulation parameters.
      - name: ACES Color Management
        description: Blender integrates with OpenColorIO for ACES and professional color pipeline support in VFX productions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
