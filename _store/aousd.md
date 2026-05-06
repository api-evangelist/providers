---
name: Alliance for OpenUSD
description: The Alliance for OpenUSD (AOUSD) is a Linux Foundation project dedicated to promoting interoperability of 3D content through Universal Scene Description (OpenUSD). Founded by Pixar, Adobe, Apple, Autodesk, and NVIDIA, AOUSD standardizes 3D content ecosystems for film, gaming, architecture, industrial design, and the metaverse. OpenUSD provides a high-performance extensible software platform for collaboratively constructing animated 3D scenes with schemas for geometry, shading, lighting, physics, and volume rendering.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 3D
  - Interoperability
  - Linux Foundation
  - Metaverse
  - OpenUSD
  - Specification
  - Standards
  - USD
  - Visual Effects
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/apis.yml
specificationVersion: '0.16'
apis:
  - name: OpenUSD C++ API
    description: The OpenUSD C++ API is the primary interface for working with Universal Scene Description data. Provides access to USD core (scene composition and asset management), UsdImaging and Hydra (rendering infrastructure), schema APIs for geometry (UsdGeom), shading (UsdShade), lighting (UsdLux), physics (UsdPhysics), volume (UsdVol), and the Shader Discovery and Registry (SDR). Available as an open-source library under the Apache 2.0 license.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://openusd.org/release/api/index.html
    baseURL: https://openusd.org
    tags:
      - 3D
      - C++
      - File Format
      - Library
      - OpenUSD
      - Rendering
      - Scene Description
    properties:
      - type: Documentation
        url: https://openusd.org/release/api/index.html
      - type: APIReference
        url: https://openusd.org/release/api/index.html
      - type: GettingStarted
        url: https://openusd.org/release/tut_usd_tutorials.html
      - type: GitHubRepository
        url: https://github.com/PixarAnimationStudios/OpenUSD
      - type: Glossary
        url: https://openusd.org/release/glossary.html
    contact:
      - FN: AOUSD Community
        url: https://aousd.org/
  - name: OpenUSD Python Bindings
    description: OpenUSD provides comprehensive Python bindings for all major C++ modules, enabling scripting and pipeline integration in Python-based DCC workflows. Python bindings cover the full USD API including pxr.Usd, pxr.UsdGeom, pxr.UsdShade, pxr.UsdLux, pxr.UsdPhysics, pxr.Sdf, and Hydra. Used extensively in production pipelines at Pixar, ILM, and other studios.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://openusd.org/release/api/index.html
    baseURL: https://pypi.org/project/usd-core/
    tags:
      - 3D
      - OpenUSD
      - Python
      - Scene Description
    properties:
      - type: Documentation
        url: https://openusd.org/release/api/index.html
      - type: SDK
        url: https://pypi.org/project/usd-core/
      - type: GitHubRepository
        url: https://github.com/PixarAnimationStudios/OpenUSD
    contact:
      - FN: Pixar Animation Studios
        url: https://github.com/PixarAnimationStudios/OpenUSD
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://aousd.org
  - type: Documentation
    url: https://openusd.org/release/index.html
  - type: GettingStarted
    url: https://openusd.org/release/tut_usd_tutorials.html
  - type: GitHubOrganization
    url: https://github.com/PixarAnimationStudios
  - type: GitHubRepository
    url: https://github.com/PixarAnimationStudios/OpenUSD
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/json-schema/aousd-usd-layer-schema.json
    title: USD Layer Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/vocabulary/aousd-vocabulary.yaml
  - type: Features
    data:
      - name: Scene Composition
        description: USD's composition arcs (references, payloads, variants, instancing, and specializes) enable non-destructive scene assembly from multiple asset layers with override workflows.
      - name: Schema-Driven Extensibility
        description: OpenUSD's schema system allows studios and tool vendors to extend the core specification with domain-specific schemas for physics, simulation, characters, and environments.
      - name: Hydra Rendering Architecture
        description: The Hydra rendering delegate architecture enables pluggable render backends including Storm (OpenGL), Arnold, RenderMan, and others.
      - name: Multiple File Formats
        description: OpenUSD supports human-readable ASCII (.usda), binary (.usdb), and packaged archive (.usdz) file formats for different use cases.
      - name: Asset Resolution
        description: The ArResolver system enables customizable asset path resolution for integrating USD with studio asset management systems.
  - type: UseCases
    data:
      - name: Film and Visual Effects Production
        description: Exchange complex animated scenes between DCC tools (Maya, Houdini, Blender, Katana) and render farms using OpenUSD as the common format.
      - name: Game Development
        description: Use OpenUSD as an interchange format between game engines like Unreal Engine and Unity and DCC content creation tools.
      - name: Architecture and Design Visualization
        description: Share 3D building models, materials, and lighting between architectural design tools and real-time visualization platforms.
      - name: Metaverse and XR
        description: Enable interoperability of 3D assets and scenes across XR platforms, spatial computing devices, and virtual world applications.
      - name: Industrial Digital Twins
        description: Represent complex mechanical assemblies and simulation environments for industrial digital twin applications using USD schemas.
  - type: Integrations
    data:
      - name: Autodesk Maya / 3ds Max
        description: Import and export USD files via Autodesk's official USD plugins for Maya and 3ds Max, enabling OpenUSD-based pipelines.
      - name: SideFX Houdini
        description: Native USD integration in Houdini via LOPs (Layout Object Primitives) for creating and editing USD scenes and assets.
      - name: Apple Reality Composer Pro
        description: Apple's spatial computing tools use .usdz as the primary format for augmented reality and visionOS content.
      - name: NVIDIA Omniverse
        description: NVIDIA Omniverse is built on OpenUSD, using it as the foundation for collaborative 3D design and industrial digital twin workflows.
      - name: Pixar RenderMan
        description: RenderMan natively reads USD scenes, making it the primary production renderer for USD-based feature film pipelines.
---
