---
aid: the-color-api
name: The Color API
description: Pass in any valid color and get conversion into any other format, the name of the color, placeholder images and a multitude of schemes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Colors
  - Design
  - Utilities
created: '2025-02-12'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/the-color-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-color-api:the-color-api
    name: The Color API
    description: Free, public REST API providing color information for any input color. Returns all color format conversions (hex, RGB, HSL, HSV, CMYK, XYZ), nearest named color, placeholder image URLs, contrast color, and harmonious color schemes based on color-wheel relationships. No authentication required.
    humanURL: https://www.thecolorapi.com/
    baseURL: https://www.thecolorapi.com
    tags:
      - Colors
      - Color Conversion
      - Color Schemes
      - Design
      - Utilities
    properties:
      - type: Documentation
        url: https://www.thecolorapi.com/docs
      - type: Website
        url: https://www.thecolorapi.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/the-color-api/refs/heads/main/openapi/the-color-api-openapi.yml
    features:
      - Color Format Conversion (Hex, RGB, HSL, HSV, CMYK, XYZ)
      - Named Color Lookup
      - Color Scheme Generation
      - Multiple Scheme Modes (Monochrome, Complement, Analogic, Triad, Quad)
      - SVG and HTML Output Formats
      - JSONP Support
      - No Authentication Required
    useCases:
      - Design Tools and Color Pickers
      - Brand Color Validation
      - Accessibility Contrast Checking
      - Color Palette Generation
      - CSS Preprocessor Tooling
      - Design System Management
common:
  - type: Website
    url: https://www.thecolorapi.com/
  - type: Documentation
    url: https://www.thecolorapi.com/docs
  - type: GitHub Organization
    url: https://github.com/joshbeckman
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/the-color-api/refs/heads/main/openapi/the-color-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
