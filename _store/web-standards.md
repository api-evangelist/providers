---
aid: web-standards
name: Web Standards
description: Specifications and guidelines that define how web technologies should work, ensuring interoperability and consistency across browsers and platforms. Web standards are developed by organizations like W3C, WHATWG, IETF, and ECMA International. This topic covers the full landscape of web standards including HTML, CSS, JavaScript APIs, networking, security, graphics, media, and emerging technologies.
type: Index
url: https://www.w3.org/standards/
tags:
  - Browser Compatibility
  - CSS
  - HTML
  - Interoperability
  - JavaScript
  - Standards
  - Web APIs
  - Web Development
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: web-standards:whatwg-html
    name: WHATWG HTML Living Standard
    description: The core markup language of the web, including Web Workers, localStorage, history, the canvas element, forms, and numerous JavaScript APIs. Maintained by WHATWG and published as a continuously updated Living Standard.
    humanURL: https://html.spec.whatwg.org/multipage/
    tags:
      - HTML
      - Living Standard
      - WHATWG
      - Web APIs
    properties:
      - type: Documentation
        url: https://html.spec.whatwg.org/multipage/
      - type: GitHubRepository
        url: https://github.com/whatwg/html
  - aid: web-standards:whatwg-fetch
    name: WHATWG Fetch Living Standard
    description: The networking model for resource retrieval on the web. Defines the Fetch API used by browsers and JavaScript to make HTTP requests, replacing the older XMLHttpRequest API.
    humanURL: https://fetch.spec.whatwg.org/
    tags:
      - Fetch API
      - HTTP
      - Living Standard
      - Networking
      - WHATWG
    properties:
      - type: Documentation
        url: https://fetch.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/fetch
  - aid: web-standards:whatwg-dom
    name: WHATWG DOM Living Standard
    description: The core infrastructure used to define the web. Specifies the Document Object Model (DOM), which represents HTML/XML documents as a tree of nodes that scripts can manipulate.
    humanURL: https://dom.spec.whatwg.org/
    tags:
      - DOM
      - Living Standard
      - WHATWG
      - Web APIs
    properties:
      - type: Documentation
        url: https://dom.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/dom
  - aid: web-standards:whatwg-url
    name: WHATWG URL Living Standard
    description: Infrastructure and algorithms around URLs on the web. Defines how URLs are parsed, serialized, and resolved, and specifies the URL and URLSearchParams APIs.
    humanURL: https://url.spec.whatwg.org/
    tags:
      - Living Standard
      - URL
      - WHATWG
    properties:
      - type: Documentation
        url: https://url.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/url
  - aid: web-standards:whatwg-streams
    name: WHATWG Streams Living Standard
    description: APIs for creating, composing, and consuming streams of data. Defines ReadableStream, WritableStream, and TransformStream interfaces for efficient data processing.
    humanURL: https://streams.spec.whatwg.org/
    tags:
      - Living Standard
      - Streaming
      - WHATWG
      - Web APIs
    properties:
      - type: Documentation
        url: https://streams.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/streams
  - aid: web-standards:whatwg-websockets
    name: WHATWG WebSockets Living Standard
    description: APIs to enable web applications to maintain bidirectional communications with server-side processes. Defines the WebSocket interface for full-duplex communication channels over a single TCP connection.
    humanURL: https://websockets.spec.whatwg.org/
    tags:
      - Living Standard
      - Real-Time
      - WebSockets
      - WHATWG
    properties:
      - type: Documentation
        url: https://websockets.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/websockets
  - aid: web-standards:whatwg-storage
    name: WHATWG Storage Living Standard
    description: Persistent storage API, quota management, and platform storage architecture. Defines how web applications can store data persistently and manage storage quotas.
    humanURL: https://storage.spec.whatwg.org/
    tags:
      - Living Standard
      - Storage
      - WHATWG
      - Web APIs
    properties:
      - type: Documentation
        url: https://storage.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/storage
  - aid: web-standards:whatwg-encoding
    name: WHATWG Encoding Living Standard
    description: Character encoding functionality on the web. Defines the TextEncoder and TextDecoder APIs for converting between strings and binary data using various character encodings.
    humanURL: https://encoding.spec.whatwg.org/
    tags:
      - Character Encoding
      - Living Standard
      - WHATWG
    properties:
      - type: Documentation
        url: https://encoding.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/encoding
  - aid: web-standards:whatwg-notifications
    name: WHATWG Notifications API Living Standard
    description: Provides an API allowing web pages to control the display of system notifications to end users, enabling alerts outside the context of a web page.
    humanURL: https://notifications.spec.whatwg.org/
    tags:
      - Living Standard
      - Notifications
      - WHATWG
    properties:
      - type: Documentation
        url: https://notifications.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/notifications
  - aid: web-standards:whatwg-file-system
    name: WHATWG File System Living Standard
    description: Infrastructure and API for accessing the file system. Provides FileSystemHandle, FileSystemFileHandle, and FileSystemDirectoryHandle interfaces for reading and writing files on the user's local device.
    humanURL: https://fs.spec.whatwg.org/
    tags:
      - File System
      - Living Standard
      - Storage
      - WHATWG
    properties:
      - type: Documentation
        url: https://fs.spec.whatwg.org/
      - type: GitHubRepository
        url: https://github.com/whatwg/fs
  - aid: web-standards:w3c-css
    name: W3C CSS Specifications
    description: Cascading Style Sheets specifications developed by the W3C CSS Working Group. Covers layout (Flexbox, Grid), selectors, animations, transforms, custom properties, and all aspects of web presentation.
    humanURL: https://www.w3.org/Style/CSS/
    tags:
      - CSS
      - Layout
      - Styling
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/Style/CSS/
      - type: GitHubOrganization
        url: https://github.com/w3c/csswg-drafts
  - aid: web-standards:w3c-webauthn
    name: W3C Web Authentication (WebAuthn)
    description: A W3C Recommendation that defines a strong authentication API for web applications, enabling passwordless and multi-factor authentication using public key cryptography and hardware authenticators.
    humanURL: https://www.w3.org/TR/webauthn/
    tags:
      - Authentication
      - Security
      - W3C
      - WebAuthn
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/webauthn/
      - type: GitHubRepository
        url: https://github.com/w3c/webauthn
  - aid: web-standards:w3c-webrtc
    name: W3C WebRTC
    description: Web Real-Time Communications specifications enabling peer-to-peer audio, video, and data communication directly between browsers without plugins. Developed by the W3C WebRTC Working Group.
    humanURL: https://www.w3.org/TR/webrtc/
    tags:
      - Communication
      - Real-Time
      - Video
      - W3C
      - WebRTC
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/webrtc/
      - type: GitHubRepository
        url: https://github.com/w3c/webrtc-pc
  - aid: web-standards:w3c-webgpu
    name: W3C WebGPU
    description: A W3C specification providing a modern GPU-accelerated graphics and compute interface for the web. Developed by the GPU for the Web Working Group as a successor to WebGL.
    humanURL: https://www.w3.org/TR/webgpu/
    tags:
      - GPU
      - Graphics
      - W3C
      - WebGPU
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/webgpu/
      - type: GitHubRepository
        url: https://github.com/gpuweb/gpuweb
  - aid: web-standards:w3c-web-components
    name: W3C Web Components
    description: 'A suite of W3C specifications enabling reusable custom elements: Custom Elements v1, Shadow DOM, and HTML Templates. Allows developers to create encapsulated, reusable UI components.'
    humanURL: https://www.w3.org/standards/techs/components
    tags:
      - Components
      - Custom Elements
      - Shadow DOM
      - W3C
      - Web Components
    properties:
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Web_Components
      - type: GitHubRepository
        url: https://github.com/WICG/webcomponents
  - aid: web-standards:w3c-service-workers
    name: W3C Service Workers
    description: A W3C specification that enables web applications to work offline, do background synchronization, and intercept network requests. Service Workers act as a programmable network proxy between the browser and network.
    humanURL: https://www.w3.org/TR/service-workers/
    tags:
      - Offline
      - Progressive Web Apps
      - Service Workers
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/service-workers/
      - type: GitHubRepository
        url: https://github.com/w3c/ServiceWorker
  - aid: web-standards:w3c-payment-request
    name: W3C Payment Request API
    description: A W3C Recommendation that standardizes the checkout process on the web, reducing the need for forms by using browser-stored payment information and supporting multiple payment methods.
    humanURL: https://www.w3.org/TR/payment-request/
    tags:
      - Commerce
      - Payments
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/payment-request/
      - type: GitHubRepository
        url: https://github.com/w3c/payment-request
  - aid: web-standards:w3c-webassembly
    name: W3C WebAssembly
    description: A portable binary instruction format for a stack-based virtual machine. Enables near-native performance for web applications written in languages like C, C++, and Rust.
    humanURL: https://www.w3.org/TR/wasm-core-1/
    tags:
      - Performance
      - W3C
      - WebAssembly
    properties:
      - type: Documentation
        url: https://webassembly.org/
      - type: GitHubRepository
        url: https://github.com/WebAssembly/spec
  - aid: web-standards:w3c-json-ld
    name: W3C JSON-LD
    description: JSON-LD 1.1 is a W3C Recommendation for Linked Data in JSON format. Provides a method to encode Linked Data using JSON, enabling semantic interoperability and integration with the Semantic Web.
    humanURL: https://www.w3.org/TR/json-ld11/
    tags:
      - JSON-LD
      - Linked Data
      - Semantic Web
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/json-ld11/
      - type: GitHubRepository
        url: https://github.com/w3c/json-ld-syntax
  - aid: web-standards:w3c-verifiable-credentials
    name: W3C Verifiable Credentials
    description: A W3C Recommendation that defines a data model for expressing credentials on the web in a cryptographically secure, privacy-respecting, and machine-verifiable way.
    humanURL: https://www.w3.org/TR/vc-data-model/
    tags:
      - Credentials
      - Identity
      - Privacy
      - Security
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/vc-data-model/
      - type: GitHubRepository
        url: https://github.com/w3c/vc-data-model
  - aid: web-standards:w3c-web-ml
    name: W3C Web Neural Network API (WebNN)
    description: A W3C specification enabling hardware-accelerated machine learning inference directly in web browsers, providing a low-level API for neural network operations on CPUs, GPUs, and dedicated ML accelerators.
    humanURL: https://www.w3.org/TR/webnn/
    tags:
      - Artificial Intelligence
      - Machine Learning
      - W3C
      - WebNN
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/webnn/
      - type: GitHubRepository
        url: https://github.com/webmachinelearning/webnn
  - aid: web-standards:w3c-did
    name: W3C Decentralized Identifiers (DIDs)
    description: A W3C Recommendation defining a new type of identifier enabling verifiable, decentralized digital identity. DIDs are globally unique, resolvable with high availability, and cryptographically verifiable.
    humanURL: https://www.w3.org/TR/did-core/
    tags:
      - Decentralized Identity
      - DID
      - Identity
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/did-core/
      - type: GitHubRepository
        url: https://github.com/w3c/did-core
  - aid: web-standards:ietf-http
    name: IETF HTTP Specifications
    description: The IETF HTTP Working Group specifications defining the HyperText Transfer Protocol. Includes HTTP/1.1 (RFC 9110), HTTP/2 (RFC 9113), HTTP/3 (RFC 9114), and related standards for caching, cookies, and security headers.
    humanURL: https://httpwg.org/
    tags:
      - HTTP
      - IETF
      - Networking
      - Protocol
    properties:
      - type: Documentation
        url: https://httpwg.org/specs/
      - type: GitHubOrganization
        url: https://github.com/httpwg
  - aid: web-standards:ecma-javascript
    name: ECMA JavaScript (ECMAScript)
    description: The ECMAScript specification (ECMA-262) defines the JavaScript programming language. Published annually by TC39 with new features, ECMAScript is the foundation for all JavaScript runtime environments including browsers and Node.js.
    humanURL: https://ecma-international.org/publications-and-standards/standards/ecma-262/
    tags:
      - ECMAScript
      - JavaScript
      - Programming Language
      - Standards
    properties:
      - type: Documentation
        url: https://tc39.es/ecma262/
      - type: GitHubRepository
        url: https://github.com/tc39/ecma262
      - type: GitHubOrganization
        url: https://github.com/tc39
common:
  - url: https://www.w3.org/
    name: World Wide Web Consortium (W3C)
    type: Website
    description: The main standards body for web technologies.
  - url: https://whatwg.org/
    name: WHATWG
    type: Website
    description: Web Hypertext Application Technology Working Group, maintainers of Living Standards.
  - url: https://ietf.org/
    name: Internet Engineering Task Force (IETF)
    type: Website
    description: Standards body for internet protocols including HTTP.
  - url: https://ecma-international.org/
    name: ECMA International
    type: Website
    description: Standards body for ECMAScript (JavaScript) and other computing standards.
  - url: https://www.w3.org/TR/
    name: W3C Technical Reports
    type: Documentation
    description: Complete directory of all W3C specifications and standards.
  - url: https://developer.mozilla.org/en-US/docs/Web/API
    name: MDN Web APIs Reference
    type: APIReference
    description: Comprehensive reference for all Web APIs implemented in browsers.
  - url: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference
    name: MDN JavaScript Reference
    type: APIReference
    description: Reference documentation for the JavaScript language and standard library.
  - url: https://caniuse.com/
    name: Can I Use
    type: Tools
    description: Browser support tables for HTML5, CSS3, and other web standards.
  - url: https://wpt.fyi/
    name: web-platform-tests
    type: Tools
    description: Cross-browser test suite for web platform specifications.
  - url: https://github.com/web-platform-tests/wpt
    name: web-platform-tests GitHub
    type: GitHubRepository
    description: Repository for cross-browser web platform compliance test suite.
  - url: https://github.com/w3c
    name: W3C GitHub Organization
    type: GitHubOrganization
    description: GitHub organization hosting W3C specification repositories.
  - url: https://github.com/whatwg
    name: WHATWG GitHub Organization
    type: GitHubOrganization
    description: GitHub organization hosting WHATWG Living Standard repositories.
  - url: https://github.com/tc39
    name: TC39 GitHub Organization
    type: GitHubOrganization
    description: GitHub organization for ECMAScript proposals and the specification.
  - url: https://github.com/WICG
    name: WICG GitHub Organization
    type: GitHubOrganization
    description: Web Incubator Community Group for incubating new web platform features.
  - type: JSONLD
    url: json-ld/web-standards-context.jsonld
  - type: Vocabulary
    url: vocabulary/web-standards-vocabulary.yml
  - name: Web Standards Features
    type: Features
    data:
      - name: Interoperability
        description: Web standards ensure that websites and applications work consistently across all browsers and platforms.
      - name: Progressive Enhancement
        description: Standards enable building experiences that work for all users and are enhanced for capable browsers.
      - name: Security and Privacy
        description: Standards define security mechanisms like CSP, CORS, WebAuthn, and privacy-preserving APIs.
      - name: Performance APIs
        description: Standards provide APIs for measuring and optimizing web application performance.
      - name: Offline Capabilities
        description: Service Workers and Storage APIs enable web applications to function without network access.
      - name: Real-Time Communication
        description: WebRTC and WebSockets enable peer-to-peer and server communication without plugins.
      - name: Hardware Access
        description: Device APIs provide controlled access to hardware like cameras, microphones, and sensors.
      - name: Machine Learning
        description: WebNN enables hardware-accelerated ML inference directly in the browser.
  - name: Web Standards Use Cases
    type: UseCases
    data:
      - name: Progressive Web Apps
        description: Use Service Workers, Web Storage, Web Push, and Manifest specifications to build installable, offline-capable web applications.
      - name: Authentication
        description: Implement passwordless authentication with WebAuthn and Verifiable Credentials for secure, phishing-resistant login.
      - name: Real-Time Collaboration
        description: Use WebRTC, WebSockets, and Broadcast Channel API for real-time data sharing and video/audio communication.
      - name: E-Commerce
        description: Streamline checkout with Payment Request API and Web Authentication for secure, frictionless transactions.
      - name: Data Visualization
        description: Use WebGL, WebGPU, Canvas API, and SVG for high-performance, hardware-accelerated graphics and charts.
      - name: Content Management
        description: Use Streams API, Fetch API, and IndexedDB for efficient content loading, caching, and storage.
      - name: Accessibility
        description: Apply WCAG guidelines and ARIA attributes to make web content accessible to all users.
      - name: Internationalization
        description: Use Encoding API and Intl APIs to support global audiences with proper text handling.
  - name: Web Standards Integrations
    type: Integrations
    data:
      - name: Browser Vendors
        description: Chrome, Firefox, Safari, and Edge implement web standards to provide consistent capabilities across platforms.
      - name: JavaScript Runtimes
        description: Node.js, Deno, and Bun implement web standard APIs including Fetch, Streams, WebCrypto, and URL.
      - name: Server Frameworks
        description: Express, Fastify, Hono, and other frameworks align with web standard request/response models.
      - name: Build Tools
        description: Vite, Webpack, and esbuild target web standards to produce optimized web applications.
      - name: Testing Frameworks
        description: Playwright, WebDriver, and Puppeteer automate browsers using WebDriver and related specifications.
      - name: Edge Runtimes
        description: Cloudflare Workers, Vercel Edge, and Deno Deploy implement web standard APIs for edge computing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
