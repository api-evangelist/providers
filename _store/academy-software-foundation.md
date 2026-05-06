---
aid: academy-software-foundation
name: Academy Software Foundation
description: The Academy Software Foundation (ASWF) is a Linux Foundation project that supports open source software development for the motion picture, visual effects, and animation industries. ASWF hosts a portfolio of production-proven open source projects including OpenEXR, OpenVDB, OpenColorIO, OpenTimelineIO, OpenShadingLanguage, MaterialX, and more. These projects form the backbone of modern film and media production pipelines worldwide.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Animation
  - Color Management
  - Film
  - Linux Foundation
  - Open Source
  - Rendering
  - Standards
  - Visual Effects
  - VFX
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: academy-software-foundation:openexr
    name: OpenEXR
    description: OpenEXR is an open standard high-dynamic-range (HDR) image file format specification and reference implementation developed by Industrial Light and Magic. It is the industry standard for visual effects and animation and provides a C++ library for reading and writing EXR image files.
    humanURL: https://openexr.com/
    tags:
      - Image Format
      - HDR
      - Standards
      - C++
    properties:
      - type: Documentation
        url: https://openexr.com/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/openexr
  - aid: academy-software-foundation:openvdb
    name: OpenVDB
    description: OpenVDB is an Academy Award-winning open source C++ library for efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids. It is the industry standard for volumetric effects in film and visual effects production.
    humanURL: https://www.openvdb.org/
    tags:
      - Volumetric Data
      - C++
      - Rendering
      - Standards
    properties:
      - type: Documentation
        url: https://www.openvdb.org/documentation/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/openvdb
  - aid: academy-software-foundation:opencolorio
    name: OpenColorIO
    description: OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production, enabling color transforms and image display to be handled in a consistent manner across many applications. It is used by major VFX studios and DCC tools including Maya, Nuke, and Houdini.
    humanURL: https://opencolorio.org/
    tags:
      - Color Management
      - Standards
      - C++
    properties:
      - type: Documentation
        url: https://opencolorio.readthedocs.io/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenColorIO
  - aid: academy-software-foundation:opentimelineio
    name: OpenTimelineIO
    description: OpenTimelineIO (OTIO) is an open source API and interchange format for editorial timeline information. It is designed to be more expressive than existing formats while still being easy to read and write, enabling better interoperability between editing tools.
    humanURL: https://opentimeline.io/
    tags:
      - Editorial
      - Timeline
      - Standards
      - Python
    properties:
      - type: Documentation
        url: https://opentimelineio.readthedocs.io/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
  - aid: academy-software-foundation:openshadinglanguage
    name: Open Shading Language
    description: Open Shading Language (OSL) is a small but rich language for programmable shading in advanced renderers and other applications. It is ideal for describing materials, lights, displacement, and pattern generation and is supported by many production renderers.
    humanURL: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
    tags:
      - Shading
      - Rendering
      - Standards
      - C++
    properties:
      - type: Documentation
        url: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/blob/main/src/doc/osl-languagespec.pdf
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
  - aid: academy-software-foundation:materialx
    name: MaterialX
    description: MaterialX is an open standard for the exchange of rich material and look-development content between applications and renderers. It provides a language for defining surface and volume shading patterns that can be used across different rendering systems and DCC applications.
    humanURL: https://www.materialx.org/
    tags:
      - Materials
      - Shading
      - Standards
      - XML
    properties:
      - type: Documentation
        url: https://materialx.org/docs/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/MaterialX
  - aid: academy-software-foundation:opencue
    name: OpenCue
    description: OpenCue is an open source render management system for visual effects and animation productions. It enables studios to deploy and manage a render farm, schedule jobs, and track progress across large numbers of render nodes. It was originally developed by Sony Pictures Imageworks.
    humanURL: https://www.opencue.io/
    tags:
      - Render Management
      - VFX
      - Python
    properties:
      - type: Documentation
        url: https://www.opencue.io/docs/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenCue
      - url: openapi/academy-software-foundation-opencue.yaml
        type: OpenAPI
      - url: json-schema/opencue-job-schema.json
        type: JSONSchema
      - url: examples/opencue-job-example.json
        type: Example
  - aid: academy-software-foundation:openimagedio
    name: OpenImageIO
    description: OpenImageIO (OIIO) is a library for reading, writing, and processing images in a wide variety of file formats. It is used in visual effects and animation production pipelines for texture baking, image compositing, and format conversion.
    humanURL: https://sites.google.com/site/openimageio/home
    tags:
      - Image Processing
      - C++
      - VFX
    properties:
      - type: Documentation
        url: https://openimageio.readthedocs.io/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenImageIO
  - aid: academy-software-foundation:openfx
    name: OpenFX
    description: OpenFX is an open standard API for visual effects plug-ins used in compositing and image processing applications. It defines how host applications and image processing plug-ins communicate, enabling interoperability across compositing tools.
    humanURL: https://openfx.io/
    tags:
      - Visual Effects
      - Plugin API
      - Standards
      - C++
    properties:
      - type: Documentation
        url: https://openfx.io/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/openfx
  - aid: academy-software-foundation:openapv
    name: OpenAPV
    description: OpenAPV is an open, royalty-free video codec specification designed for professional video production and post-production workflows. It is optimized for high-quality intermediate video formats used in camera and on-set production pipelines.
    humanURL: https://github.com/AcademySoftwareFoundation/openapv
    tags:
      - Video Codec
      - Standards
      - C
    properties:
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/openapv
  - aid: academy-software-foundation:openpbr
    name: OpenPBR
    description: OpenPBR is an open specification and reference implementation for a physically-based shading model. It defines a standard material definition language that can be used across different renderers to achieve consistent appearance.
    humanURL: https://academysoftwarefoundation.github.io/OpenPBR/
    tags:
      - Rendering
      - Materials
      - Standards
    properties:
      - type: Documentation
        url: https://academysoftwarefoundation.github.io/OpenPBR/
      - type: GitHubRepository
        url: https://github.com/AcademySoftwareFoundation/OpenPBR
common:
  - type: Website
    url: https://www.aswf.io/
  - type: Documentation
    url: https://www.aswf.io/projects/
  - type: GitHubOrganization
    url: https://github.com/AcademySoftwareFoundation
  - type: Blog
    url: https://www.aswf.io/news/
  - type: GettingStarted
    url: https://www.aswf.io/get-involved/
  - type: TermsOfService
    url: https://www.aswf.io/terms/
  - type: PrivacyPolicy
    url: https://www.aswf.io/privacy/
  - type: Features
    data:
      - name: Open Source Governance
        description: All ASWF projects are governed by open, transparent processes under the Linux Foundation umbrella
      - name: Production-Proven Projects
        description: Projects like OpenEXR, OpenVDB, and OpenColorIO are used in major film studios worldwide
      - name: Vendor-Neutral Collaboration
        description: ASWF provides a neutral forum where studios, vendors, and developers collaborate on shared technology challenges
      - name: CI/CD Infrastructure
        description: ASWF provides shared containerized build and test infrastructure via aswf-docker for consistent CI/CD across all projects
      - name: Working Groups
        description: Dedicated working groups address cross-project topics such as CI, color interop, and language interoperability
      - name: Standards Development
        description: ASWF projects define and maintain industry standards used across the global VFX and animation pipeline
  - type: UseCases
    data:
      - name: VFX Production Pipeline
        description: OpenEXR, OpenVDB, OpenColorIO, and OSL form the core of visual effects production pipelines at major studios
      - name: Render Farm Management
        description: OpenCue enables studios to build and operate large-scale distributed render farms for animation and VFX
      - name: Color Pipeline Standardization
        description: OpenColorIO provides consistent color transforms across all DCC tools in a studio pipeline
      - name: Editorial Interchange
        description: OpenTimelineIO enables timeline data exchange between editing applications like Avid, Premiere, and DaVinci Resolve
      - name: Material Interchange
        description: MaterialX and OpenPBR enable look development assets to be transferred between different render engines
      - name: Image Format Standardization
        description: OpenEXR provides a universal HDR image format for compositing, rendering output, and archiving
  - type: Integrations
    data:
      - name: Autodesk Maya
        description: Integrates with OpenColorIO, OpenEXR, and other ASWF standards via native plug-ins
      - name: The Foundry Nuke
        description: Uses OpenColorIO, OpenEXR, and OpenFX plug-ins extensively in compositing workflows
      - name: SideFX Houdini
        description: Deep integration with OpenVDB, OpenColorIO, and OpenEXR for VFX and simulation workflows
      - name: Blender
        description: Uses OpenEXR, OpenColorIO, OpenShadingLanguage, and OpenVDB for rendering and compositing
      - name: Pixar USD
        description: Works alongside ASWF standards as part of the broader VFX open source ecosystem
      - name: NVIDIA Omniverse
        description: Uses MaterialX and OpenColorIO for material interchange and color management
  - url: rules/academy-software-foundation-spectral-rules.yml
    type: SpectralRules
  - url: capabilities/render-farm-management.yaml
    type: NaftikoCapability
  - url: vocabulary/academy-software-foundation-vocabulary.yaml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
