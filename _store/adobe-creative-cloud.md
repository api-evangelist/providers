---
name: Adobe Creative Cloud
description: Adobe Creative Cloud is a collection of software and services for graphic design, video editing, web development, and photography, offering cloud-based access to Adobe's creative applications.
image: https://www.adobe.com/content/dam/cc/icons/cc-app-icon.svg
url: https://www.adobe.com/creativecloud.html
created: '2024'
modified: '2024'
specificationVersion: '0.18'
apis:
- name: Adobe Creative Cloud API
  description: Main API for accessing Adobe Creative Cloud services, managing user accounts, and integrating Creative Cloud functionality into applications.
  image: https://www.adobe.com/content/dam/cc/icons/cc-app-icon.svg
  baseURL: https://api.adobe.io/
  humanURL: https://developer.adobe.com/creative-cloud/
  tags:
  - Creative
  - Design
  - Cloud Storage
  - Assets
  properties:
  - type: Documentation
    url: https://developer.adobe.com/creative-cloud/docs/
  - type: OpenAPI
    url: https://developer.adobe.com/creative-cloud/openapi/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- name: Adobe Photoshop API
  description: Automate Photoshop workflows including generating cutouts, applying edits, and creating composites using cloud-based image processing.
  baseURL: https://image.adobe.io/
  humanURL: https://developer.adobe.com/photoshop/
  tags:
  - Image Processing
  - Photoshop
  - Automation
  properties:
  - type: Documentation
    url: https://developer.adobe.com/photoshop/photoshop-api-docs/
  - type: API Reference
    url: https://developer.adobe.com/photoshop/photoshop-api-docs/api/
- name: Adobe Lightroom API
  description: API for managing photos, albums, and applying presets in Adobe Lightroom, enabling automated photo organization and editing workflows.
  baseURL: https://lr.adobe.io/
  humanURL: https://developer.adobe.com/lightroom/
  tags:
  - Photography
  - Photo Management
  - Image Editing
  properties:
  - type: Documentation
    url: https://developer.adobe.com/lightroom/lightroom-api-docs/
  - type: API Reference
    url: https://developer.adobe.com/lightroom/lightroom-api-docs/api/
- name: Adobe Stock API
  description: Search, license, and integrate Adobe Stock assets including photos, vectors, illustrations, and videos into applications and workflows.
  baseURL: https://stock.adobe.io/
  humanURL: https://developer.adobe.com/stock/
  tags:
  - Stock Photos
  - Assets
  - Licensing
  - Media
  properties:
  - type: Documentation
    url: https://developer.adobe.com/stock/docs/
  - type: API Reference
    url: https://developer.adobe.com/stock/docs/api/
  - type: Search
    url: https://developer.adobe.com/stock/docs/api/search/
- name: Adobe Fonts API
  description: Access and integrate Adobe Fonts (formerly Typekit) into applications, allowing users to browse and use fonts from Adobe's library.
  baseURL: https://typekit.com/api/
  humanURL: https://developer.adobe.com/fonts/
  tags:
  - Fonts
  - Typography
  - Web Fonts
  properties:
  - type: Documentation
    url: https://developer.adobe.com/fonts/docs/
  - type: API Reference
    url: https://developer.adobe.com/fonts/docs/api/
- name: Adobe PDF Services API
  description: Create, convert, OCR, and manipulate PDF documents programmatically with cloud-based PDF processing capabilities.
  baseURL: https://pdf-services.adobe.io/
  humanURL: https://developer.adobe.com/document-services/apis/pdf-services/
  tags:
  - PDF
  - Document Processing
  - OCR
  - Conversion
  properties:
  - type: Documentation
    url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/
  - type: API Reference
    url: https://developer.adobe.com/document-services/docs/apis/
- name: Creative Cloud Libraries API
  description: Access and manage Creative Cloud Libraries, enabling synchronization of colors, text styles, graphics, and other creative assets across applications.
  baseURL: https://cc-libraries.adobe.io/
  humanURL: https://developer.adobe.com/creative-cloud-libraries/
  tags:
  - Libraries
  - Assets
  - Collaboration
  - Sync
  properties:
  - type: Documentation
    url: https://developer.adobe.com/creative-cloud-libraries/docs/
  - type: API Reference
    url: https://developer.adobe.com/creative-cloud-libraries/docs/api/
common:
- type: Developer Portal
  url: https://developer.adobe.com/
- type: Console
  url: https://developer.adobe.com/console/
- type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- type: Terms of Service
  url: https://www.adobe.com/legal/terms.html
- type: Privacy Policy
  url: https://www.adobe.com/privacy.html
- type: Support
  url: https://developer.adobe.com/support/
- type: Blog
  url: https://blog.developer.adobe.com/
- type: Status
  url: https://status.adobe.com/
maintainers:
- FN: Adobe Developer Team
  email: dev-support@adobe.com
  url: https://developer.adobe.com/
tags:
- Creative
- Design
- Photography
- Video
- Documents
- Cloud
- SaaS
---