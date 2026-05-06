---
aid: javascript
name: JavaScript
description: JavaScript is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions. It is a multi-paradigm, dynamic language supporting object-oriented, imperative, and declarative programming styles. The JavaScript Web APIs are a collection of browser-provided interfaces that enable web applications to interact with the browser, the operating system, and remote services. They include the Fetch API, Web Storage, WebSockets, Canvas API, Web Audio API, Geolocation, Notifications, IndexedDB, and many more standardized interfaces maintained by the WHATWG and the W3C.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Browser
  - ECMAScript
  - JavaScript
  - Programming Language
  - Web APIs
url: https://raw.githubusercontent.com/api-evangelist/javascript/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: javascript:fetch-api
    name: Fetch API
    description: Modern JavaScript interface for making HTTP requests and processing responses, providing a more powerful and flexible replacement for XMLHttpRequest.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
    tags:
      - AJAX
      - Async
      - HTTP
      - Network
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
      - type: Specification
        url: https://fetch.spec.whatwg.org/
  - aid: javascript:web-storage-api
    name: Web Storage API
    description: JavaScript APIs for storing key/value pairs in the browser using localStorage and sessionStorage.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
    tags:
      - Browser
      - Client-side
      - Storage
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API
      - type: Specification
        url: https://html.spec.whatwg.org/multipage/webstorage.html
  - aid: javascript:web-audio-api
    name: Web Audio API
    description: JavaScript system for controlling audio on the web, allowing developers to choose audio sources, add effects, create visualizations, and apply spatial effects.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API
    tags:
      - Audio
      - Media
      - Sound
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API
      - type: Specification
        url: https://webaudio.github.io/web-audio-api/
  - aid: javascript:canvas-api
    name: Canvas API
    description: JavaScript APIs for drawing graphics via the HTML canvas element, supporting 2D shapes, text, images, and animations.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
    tags:
      - 2D
      - Drawing
      - Graphics
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial
      - type: Specification
        url: https://html.spec.whatwg.org/multipage/canvas.html
  - aid: javascript:websockets-api
    name: WebSockets API
    description: JavaScript API for opening bidirectional, full-duplex communication channels over a single TCP connection between client and server.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
    tags:
      - Bidirectional
      - Communication
      - Real-time
      - WebSocket
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
      - type: Specification
        url: https://websockets.spec.whatwg.org/
  - aid: javascript:geolocation-api
    name: Geolocation API
    description: JavaScript API for accessing geographical position information of the device, with user consent.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
    tags:
      - GPS
      - Location
      - Position
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API
      - type: Specification
        url: https://w3c.github.io/geolocation-api/
  - aid: javascript:notifications-api
    name: Notifications API
    description: JavaScript API for displaying system notifications to users outside the context of the browser tab.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API
    tags:
      - Alerts
      - Notifications
      - User Interface
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API
      - type: Specification
        url: https://notifications.spec.whatwg.org/
  - aid: javascript:indexeddb-api
    name: IndexedDB API
    description: Low-level JavaScript API for client-side storage of significant amounts of structured data, including files and blobs.
    humanURL: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
    tags:
      - Client-side
      - Database
      - NoSQL
      - Storage
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB
      - type: Specification
        url: https://w3c.github.io/IndexedDB/
common:
  - type: Website
    url: https://www.javascript.com/
  - type: Documentation
    url: https://developer.mozilla.org/en-US/docs/Web/JavaScript
  - type: Getting Started
    url: https://developer.mozilla.org/en-US/docs/Learn/JavaScript
  - type: Reference
    url: https://developer.mozilla.org/en-US/docs/Web/API
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
