---
aid: teledyne-technologies
name: Teledyne Technologies
description: Teledyne Technologies Incorporated is a leading provider of sophisticated digital imaging products and software, instrumentation, aerospace and defense electronics, and engineered systems. Headquartered in Thousand Oaks, California, Teledyne serves the defense, commercial, and industrial markets. Key subsidiaries include Teledyne FLIR (thermal imaging cameras and systems), Teledyne LeCroy (oscilloscopes and protocol analyzers), Teledyne Imaging (scientific and industrial cameras), and Teledyne API (air quality monitoring instruments). Teledyne FLIR provides REST APIs and SDKs for thermal camera integration, while Teledyne LeCroy provides ActiveDSO and VISA-based automation APIs for test and measurement instruments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Aerospace
  - Defense
  - Digital Imaging
  - Instrumentation
  - Thermal Imaging
  - Test and Measurement
  - Fortune 500
url: https://raw.githubusercontent.com/api-evangelist/teledyne-technologies/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: teledyne-technologies:flir-camera-rest-api
    name: Teledyne FLIR Camera REST API
    description: Teledyne FLIR provides REST API access for automation cameras (A50/A70, A400/A500/A700, Ax8 series). The API enables retrieval of thermal images, region of interest (ROI) data, alarm data, and camera configuration. Endpoints return radiometric JPEG images and JSON data for temperature measurements across spots, boxes, lines, polylines, and delta measurements. Used for industrial process monitoring, building inspection, and predictive maintenance applications. A Swagger/OpenAPI JSON specification is available from the camera's local web server.
    humanURL: https://www.flir.com/support-center/Instruments/restful-api-exercise/
    baseURL: http://{camera_ip}/api
    tags:
      - Thermal Imaging
      - Camera
      - REST API
      - Industrial
      - Machine Vision
    properties:
      - type: Documentation
        url: https://www.flir.com/support-center/Instruments/restful-api-exercise/
      - type: OpenAPI
        url: openapi/teledyne-flir-camera-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/teledyne-flir-measurement-schema.json
      - type: JSONSchema
        url: json-schema/teledyne-flir-alarm-schema.json
  - aid: teledyne-technologies:flir-spinnaker-sdk
    name: Teledyne FLIR Spinnaker SDK
    description: The Spinnaker SDK provides programmatic control of Teledyne FLIR and DALSA machine vision cameras over USB3, GigE, 5GigE, and 10GigE interfaces. Supports C++, C#, Python, and Java with a cross-platform API for camera discovery, configuration, image acquisition, and processing. Includes SpinView GUI for camera exploration and real-time viewing. Used for factory automation, quality inspection, and scientific imaging applications.
    humanURL: https://www.flir.com/support/browse/camera-cores--components/machine-vision-cameras/sdks
    baseURL: https://www.flir.com
    tags:
      - Machine Vision
      - Camera
      - SDK
      - Industrial Automation
      - Image Acquisition
    properties:
      - type: Documentation
        url: https://www.flir.com/support/browse/camera-cores--components/machine-vision-cameras/sdks
      - type: SDK
        url: https://www.flir.com/support/browse/camera-cores--components/machine-vision-cameras/sdks
      - type: GitHub
        url: https://github.com/Teledyne-MV/Spinnaker-Examples
  - aid: teledyne-technologies:flir-mobile-sdk
    name: Teledyne FLIR Mobile SDK
    description: The FLIR Mobile SDK enables iOS and Android developers to build mobile applications that integrate thermal imaging capabilities from Teledyne FLIR professional thermal cameras. Supports data collection from connected thermal cameras and metering devices. Available through FLIR's Developer Program with approved access. Includes an App Gallery for showcasing third-party thermal imaging applications.
    humanURL: https://www.flir.com/developer/mobile-sdk/
    baseURL: https://www.flir.com/developer
    tags:
      - Mobile SDK
      - iOS
      - Android
      - Thermal Imaging
      - Developer Program
    properties:
      - type: Documentation
        url: https://www.flir.com/developer/mobile-sdk/
      - type: DeveloperPortal
        url: https://www.flir.com/developer/mobile-sdk/
  - aid: teledyne-technologies:lecroy-activedso-api
    name: Teledyne LeCroy ActiveDSO API
    description: ActiveDSO is Teledyne LeCroy's ActiveX/COM control enabling remote automation of MAUI-based oscilloscopes from Windows applications via SCPI commands, VISA drivers, Ethernet (ENET), GPIB, and USBTMC interfaces. Supports Python, C++, C#, LabVIEW, and MATLAB automation. Used for automated test sequences, waveform capture, protocol analysis, and measurement reporting in test and measurement workflows.
    humanURL: https://www.teledynelecroy.com/support/techlib/programmingexamples.aspx
    baseURL: https://www.teledynelecroy.com
    tags:
      - Oscilloscope
      - Test and Measurement
      - Automation
      - SCPI
      - VISA
    properties:
      - type: Documentation
        url: https://www.teledynelecroy.com/support/techlib/programmingexamples.aspx
      - type: Documentation
        url: https://cdn.teledynelecroy.com/files/manuals/activedso-developers-guide.pdf
common:
  - url: https://www.teledyne.com/en-us
    name: Teledyne Technologies
    type: Website
    description: Teledyne Technologies corporate website.
  - url: https://www.flir.com/developer/mobile-sdk/
    name: Teledyne FLIR Developer Program
    type: DeveloperPortal
    description: FLIR Mobile SDK and developer resources.
  - url: https://github.com/FLIR
    name: Teledyne FLIR GitHub
    type: GitHub
    description: Teledyne FLIR official GitHub organization.
  - url: https://github.com/Teledyne-MV
    name: Teledyne Machine Vision GitHub
    type: GitHub
    description: Teledyne Machine Vision GitHub organization (Spinnaker SDK examples).
  - url: https://www.teledynelecroy.com/
    name: Teledyne LeCroy
    type: Website
    description: Teledyne LeCroy oscilloscopes and protocol analyzers.
  - url: https://www.teledyneimaging.com/
    name: Teledyne Imaging
    type: Website
    description: Teledyne Imaging scientific and industrial cameras.
  - url: https://www.teledyne-api.com/en-us
    name: Teledyne API
    type: Website
    description: Teledyne API air quality monitoring instruments.
  - url: https://www.linkedin.com/company/teledyne-technologies
    name: Teledyne Technologies on LinkedIn
    type: LinkedIn
    description: Teledyne Technologies LinkedIn company page.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
