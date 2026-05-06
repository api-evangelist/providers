---
aid: microsoft-windows-10
name: Microsoft Windows 10
description: Collection of APIs and developer resources for building applications on the Windows 10 platform, including Universal Windows Platform (UWP), Win32, and Windows Runtime APIs for desktop, mobile, and IoT applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
url: https://developer.microsoft.com/en-us/windows/
tags:
  - Desktop
  - Operating System
  - UWP
  - Win32
  - Windows
apis:
  - name: Windows Runtime (WinRT) API
    description: Modern API surface for building Universal Windows Platform (UWP) applications that run across all Windows 10 device families. WinRT provides a type system, APIs, and runtime environment for building apps using C#, C++, Visual Basic, and JavaScript.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/
    baseURL: https://api.windows.com
    tags:
      - Universal Apps
      - UWP
      - Windows Runtime
      - WinRT
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/uwp/api/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/uwp/get-started/
      - type: Samples
        url: https://github.com/Microsoft/Windows-universal-samples
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/
      - type: SDKs
        url: https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-winrt-openapi.yml
  - name: Win32 API
    description: Core Windows API for building traditional desktop applications using C and C++. Win32 provides direct access to system-level functionality including window management, graphics, networking, and hardware.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/
    baseURL: https://api.windows.com
    tags:
      - Desktop
      - Native
      - System Programming
      - Win32
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/apiindex/windows-api-list
      - type: Reference
        url: https://learn.microsoft.com/en-us/windows/win32/api/
      - type: Samples
        url: https://github.com/microsoft/Windows-classic-samples
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/win32/desktop-programming
      - type: OpenAPI
        url: openapi/microsoft-windows-10-win32-openapi.yml
  - name: Windows Notifications API
    description: API for sending and managing toast notifications, tile notifications, and badge updates in Windows 10 applications. Supports adaptive and interactive notifications with custom layouts, actions, and scheduling.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/
    baseURL: https://api.windows.com
    tags:
      - Notifications
      - Tiles
      - Toast
      - User Interface
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/adaptive-interactive-toasts
      - type: Samples
        url: https://github.com/WindowsNotifications/quickstart-sending-local-toast-win10
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/windows.ui.notifications
      - type: OpenAPI
        url: openapi/microsoft-windows-10-notifications-openapi.yml
  - name: Windows ML API
    description: API for integrating trained machine learning models into Windows applications using the ONNX format. Windows ML evaluates models locally on the device using hardware acceleration with DirectX 12.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/ai/windows-ml/
    baseURL: https://api.windows.com
    tags:
      - Artificial Intelligence
      - Inference
      - Machine Learning
      - ONNX
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/windows/ai/windows-ml/tutorials
      - type: Samples
        url: https://github.com/Microsoft/Windows-Machine-Learning
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started
      - type: OpenAPI
        url: openapi/microsoft-windows-10-ml-openapi.yml
  - name: Windows Storage API
    description: API for file system access, storage management, and data operations in Windows applications. Provides classes for reading, writing, and managing files and folders with appropriate access permissions.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/files/
    baseURL: https://api.windows.com
    tags:
      - Data Management
      - File System
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/uwp/api/windows.storage
      - type: Best Practices
        url: https://learn.microsoft.com/en-us/windows/uwp/files/best-practices-for-writing-to-files
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/uwp/files/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-storage-openapi.yml
  - name: Windows Cortana API
    description: API for integrating voice commands and Cortana digital assistant capabilities into Windows applications. Enables voice-activated interactions and custom voice command definitions.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/cortana/
    baseURL: https://api.windows.com
    tags:
      - Cortana
      - Digital Assistant
      - Voice
      - Voice Commands
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/cortana/voice-commands/vcd
      - type: Guidelines
        url: https://learn.microsoft.com/en-us/cortana/voice-commands/voicecommand-design-guidelines
      - type: OpenAPI
        url: openapi/microsoft-windows-10-cortana-openapi.yml
  - name: Windows Ink API
    description: API for pen and stylus input in Windows applications, providing inking surfaces, stroke recognition, and handwriting analysis. Supports pressure sensitivity, tilt, and barrel button interactions.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions
    baseURL: https://api.windows.com
    tags:
      - Ink
      - Input
      - Pen
      - Stylus
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/uwp/api/windows.ui.input.inking
      - type: Samples
        url: https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/SimpleInk
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions
      - type: OpenAPI
        url: openapi/microsoft-windows-10-ink-openapi.yml
  - name: Windows Composition API
    description: The Windows.UI.Composition API provides access to the visual layer between the XAML framework and the DirectX graphics layer. It enables high-performance, retained-mode graphics, effects, and animations as the foundation for UI across Windows devices.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/composition/visual-layer
    baseURL: https://api.windows.com
    tags:
      - Animations
      - Composition
      - Graphics
      - Visual Layer
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/uwp/composition/visual-layer
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/windows.ui.composition
      - type: Samples
        url: https://github.com/microsoft/Windows.UI.Composition-Win32-Samples
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/uwp/composition/using-the-visual-layer-with-xaml
      - type: OpenAPI
        url: openapi/microsoft-windows-10-composition-openapi.yml
  - name: DirectX Graphics API
    description: Low-level graphics API for building high-performance 2D and 3D rendering in Windows applications. Includes Direct3D for 3D graphics, Direct2D for 2D graphics, and DirectWrite for text rendering.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/directx
    baseURL: https://api.windows.com
    tags:
      - DirectX
      - Gaming
      - Graphics
      - Rendering
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/directx
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/win32/getting-started-with-directx-graphics
      - type: Samples
        url: https://github.com/microsoft/DirectX-Graphics-Samples
      - type: Reference
        url: https://microsoft.github.io/DirectX-Specs/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-directx-openapi.yml
  - name: Windows Media Capture API
    description: API for capturing photos, audio, and video from camera and microphone devices in Windows applications. Provides classes for previewing, recording, and processing media streams with configurable encoding settings.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/apps/develop/audio-video-camera
    baseURL: https://api.windows.com
    tags:
      - Audio
      - Camera
      - Media
      - Video Capture
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/apps/develop/audio-video-camera
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/windows.media.capture
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/win32/medfound/audio-video-capture-in-media-foundation
      - type: OpenAPI
        url: openapi/microsoft-windows-10-media-capture-openapi.yml
  - name: Windows Networking API
    description: API for network communication in Windows applications, providing support for sockets, WebSockets, HTTP clients, and background transfers. Enables TCP/UDP communication and real-time data streaming.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/networking/
    baseURL: https://api.windows.com
    tags:
      - HTTP
      - Networking
      - Sockets
      - WebSockets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/uwp/networking/which-networking-technology
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/windows.networking.sockets
      - type: Samples
        url: https://learn.microsoft.com/en-us/samples/microsoft/windows-universal-samples/websocket/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-networking-openapi.yml
  - name: Windows Bluetooth API
    description: API for Bluetooth communication in Windows applications, supporting Bluetooth Classic (RFCOMM) and Bluetooth Low Energy (GATT) protocols for connecting to and exchanging data with Bluetooth devices.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/devices-sensors/bluetooth
    baseURL: https://api.windows.com
    tags:
      - Bluetooth
      - Devices
      - IoT
      - Wireless
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/uwp/devices-sensors/bluetooth-dev-faq
      - type: Reference
        url: https://learn.microsoft.com/en-us/windows/win32/api/_bluetooth/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/win32/bluetooth/bluetooth-programming-with-windows-sockets
      - type: OpenAPI
        url: openapi/microsoft-windows-10-bluetooth-openapi.yml
  - name: Windows Geolocation API
    description: API for obtaining geographic location data in Windows applications. Provides access to latitude, longitude, altitude, heading, and speed from GNSS, Wi-Fi, cellular networks, and IP address sources.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/maps-and-location/
    baseURL: https://api.windows.com
    tags:
      - Geolocation
      - GPS
      - Location
      - Maps
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/uwp/api/windows.devices.geolocation
      - type: Reference
        url: https://learn.microsoft.com/en-us/windows/win32/locationapi/windows-location-api-portal
      - type: Samples
        url: https://learn.microsoft.com/en-us/samples/microsoft/windows-universal-samples/geolocation/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-geolocation-openapi.yml
  - name: Windows Sensors API
    description: API for accessing device sensor data including accelerometer, gyroscope, compass, light sensor, and proximity sensor. Provides a unified interface for reading sensor values and responding to sensor events.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/sensorsapi/introduction-to-the-sensor-and-location-platform-in-windows
    baseURL: https://api.windows.com
    tags:
      - Devices
      - Hardware
      - IoT
      - Sensors
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/sensorsapi/introduction-to-the-sensor-and-location-platform-in-windows
      - type: Reference
        url: https://learn.microsoft.com/en-us/uwp/api/windows.devices.sensors
      - type: OpenAPI
        url: openapi/microsoft-windows-10-sensors-openapi.yml
  - name: Windows Hello Authentication API
    description: Biometric and PIN-based authentication API that replaces passwords with strong two-factor authentication. Supports facial recognition, fingerprint scanning, and PIN-based user verification for secure sign-in.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/apps/develop/security/windows-hello
    baseURL: https://api.windows.com
    tags:
      - Authentication
      - Biometrics
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/apps/develop/security/windows-hello
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/apps/develop/security/windows-hello-auth-service
      - type: Reference
        url: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/webauthn-apis
      - type: OpenAPI
        url: openapi/microsoft-windows-10-hello-openapi.yml
  - name: WinUI API
    description: Modern native UI framework for building Windows desktop applications with the Fluent Design System. WinUI provides XAML-based controls, high-performance rendering, and supports both C# and C++ development.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/apps/winui/winui2/
    baseURL: https://api.windows.com
    tags:
      - Controls
      - Fluent Design
      - User Interface
      - XAML
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/apps/winui/winui2/
      - type: Reference
        url: https://learn.microsoft.com/en-us/windows/winui/api/microsoft.ui.xaml.controls
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/windows/apps/winui/winui2/getting-started
      - type: Samples
        url: https://github.com/microsoft/microsoft-ui-xaml
      - type: OpenAPI
        url: openapi/microsoft-windows-10-winui-openapi.yml
  - name: Windows Background Tasks API
    description: API for running code in the background when an application is suspended or not running. Supports time-triggered, system-triggered, and maintenance-triggered background tasks for continuous processing.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/applifecycle/background-tasks
    baseURL: https://api.windows.com
    tags:
      - App Lifecycle
      - Background Tasks
      - Scheduling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/applifecycle/background-tasks
      - type: Samples
        url: https://learn.microsoft.com/en-us/samples/microsoft/windows-universal-samples/backgroundtask/
      - type: OpenAPI
        url: openapi/microsoft-windows-10-background-tasks-openapi.yml
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/windows/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/windows/apps/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/windows/apps/get-started/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/windows/apps/develop/security/windows-hello
  - type: Blog
    url: https://blogs.windows.com/windowsdeveloper/
  - type: Status
    url: https://status.cloud.microsoft/
  - type: Support
    url: https://developer.microsoft.com/en-us/windows/support
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://www.microsoft.com/en-us/privacy/privacystatement
  - type: GitHub Organization
    url: https://github.com/microsoft
  - type: Community
    url: https://developer.microsoft.com/en-us/windows/community/
  - type: Website
    url: https://www.microsoft.com
  - type: Login
    url: https://login.microsoftonline.com/
  - type: Sign Up
    url: https://developer.microsoft.com/en-us/
  - type: SDKs
    url: https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/windows/apps/whats-new/whats-new-for-developers
  - type: Reference
    url: https://learn.microsoft.com/en-us/windows/apps/api-reference/
  - type: JSON-LD
    url: json-ld/microsoft-windows-10-context.jsonld
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-notification-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-storage-item-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-geolocation-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-sensor-reading-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-ml-model-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-windows-10-bluetooth-device-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
