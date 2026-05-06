---
aid: w3c
url: https://raw.githubusercontent.com/api-evangelist/w3c/refs/heads/main/apis.yml
name: W3C
description: The World Wide Web Consortium (W3C) is the main international standards body for the World Wide Web, founded by Tim Berners-Lee in 1994. W3C develops web standards and guidelines to ensure the long-term growth of the Web, focusing on accessibility, internationalization, privacy, and security. W3C specifications include HTML, CSS, XML, SVG, WebAssembly, ARIA, WCAG, JSON-LD, Verifiable Credentials, and hundreds of other foundational web technologies. W3C operates through Working Groups, Interest Groups, and Community Groups that develop specifications through a consensus-based process, resulting in W3C Recommendations.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accessibility
  - Standards
  - Web
  - Web Standards
created: '2025-08-25'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
apis:
  - aid: w3c:w3c-api
    name: W3C API
    description: The W3C API provides programmatic access to W3C data including specifications, working groups, editors, translations, and affiliations. It enables developers to query W3C's catalog of technical reports, discover active working groups, find specification editors and contributors, and access specification version history and status information.
    humanURL: https://api.w3.org/
    baseUrl: https://api.w3.org/
    tags:
      - API
      - Data
      - Specifications
      - Standards
      - W3C
    properties:
      - url: https://api.w3.org/doc
        type: Documentation
      - url: https://api.w3.org/
        type: BaseURL
      - url: https://github.com/w3c/w3c-api
        type: GitHub
  - aid: w3c:wcag
    name: Web Content Accessibility Guidelines (WCAG)
    description: WCAG is the international standard for web accessibility, providing guidelines for making web content more accessible to people with disabilities. WCAG 2.2 is the current Recommendation, with WCAG 3.0 in development. Guidelines cover perceivability, operability, understandability, and robustness (POUR).
    humanURL: https://www.w3.org/TR/WCAG22/
    tags:
      - Accessibility
      - Guidelines
      - Standards
      - W3C
    properties:
      - url: https://www.w3.org/TR/WCAG22/
        type: Specification
      - url: https://www.w3.org/WAI/standards-guidelines/wcag/
        type: Documentation
      - url: https://github.com/w3c/wcag
        type: GitHub
  - aid: w3c:html
    name: HTML Living Standard
    description: The HyperText Markup Language specification maintained by WHATWG as a living standard, published as a W3C Recommendation. HTML defines the semantic structure of web pages and forms the foundation of the web platform.
    humanURL: https://html.spec.whatwg.org/
    tags:
      - HTML
      - Standards
      - Web Platform
    properties:
      - url: https://html.spec.whatwg.org/
        type: Specification
      - url: https://www.w3.org/TR/html52/
        type: W3C Recommendation
      - url: https://github.com/whatwg/html
        type: GitHub
  - aid: w3c:css
    name: CSS Specifications
    description: The Cascading Style Sheets (CSS) specification family maintained by the W3C CSS Working Group. CSS defines the presentation and styling of HTML documents. Key modules include CSS Grid Layout, Flexbox, Custom Properties, Animations, and CSS Functions and Mixins.
    humanURL: https://www.w3.org/Style/CSS/
    tags:
      - CSS
      - Standards
      - Styling
      - Web Platform
    properties:
      - url: https://www.w3.org/TR/CSS/
        type: Specification
      - url: https://www.w3.org/Style/CSS/Overview.en.html
        type: Documentation
      - url: https://github.com/w3c/csswg-drafts
        type: GitHub
  - aid: w3c:json-ld
    name: JSON-LD
    description: JSON-LD (JSON for Linking Data) is a W3C Recommendation for encoding linked data using JSON. It provides a way to add semantic meaning to JSON documents through the use of @context, @id, and @type keywords, enabling interoperability through shared vocabularies like schema.org.
    humanURL: https://www.w3.org/TR/json-ld11/
    tags:
      - JSON
      - Linked Data
      - Semantic Web
      - Standards
    properties:
      - url: https://www.w3.org/TR/json-ld11/
        type: Specification
      - url: https://json-ld.org/
        type: Website
      - url: https://json-ld.org/playground/
        type: Playground
      - url: https://github.com/w3c/json-ld-syntax
        type: GitHub
  - aid: w3c:verifiable-credentials
    name: Verifiable Credentials
    description: The Verifiable Credentials Data Model is a W3C Recommendation enabling cryptographically secure, privacy-respecting digital credentials. The VC family includes the data model, data integrity proof suites, and JSON Web Token/COSE encoding methods. VC 2.0 was published as a W3C Recommendation in 2025.
    humanURL: https://www.w3.org/TR/vc-data-model-2.0/
    tags:
      - Credentials
      - Identity
      - Privacy
      - Security
      - Standards
    properties:
      - url: https://www.w3.org/TR/vc-data-model-2.0/
        type: Specification
      - url: https://www.w3.org/groups/wg/vc/
        type: Working Group
      - url: https://github.com/w3c/vc-data-model
        type: GitHub
  - aid: w3c:wasm
    name: WebAssembly
    description: WebAssembly (Wasm) is a W3C Recommendation defining a portable binary instruction format for a stack-based virtual machine. It enables near-native performance in web browsers for code compiled from languages like C, C++, and Rust, and is a core web platform technology.
    humanURL: https://www.w3.org/TR/wasm-core-2/
    tags:
      - Performance
      - Standards
      - WebAssembly
      - Web Platform
    properties:
      - url: https://www.w3.org/TR/wasm-core-2/
        type: Specification
      - url: https://webassembly.org/
        type: Website
      - url: https://github.com/WebAssembly/spec
        type: GitHub
  - aid: w3c:aria
    name: WAI-ARIA
    description: Accessible Rich Internet Applications (WAI-ARIA) is a W3C Recommendation defining a set of HTML attributes that define ways to make web content and web applications more accessible to people with disabilities. ARIA roles, states, and properties supplement HTML semantics for dynamic content.
    humanURL: https://www.w3.org/TR/wai-aria-1.2/
    tags:
      - Accessibility
      - ARIA
      - Standards
      - W3C
    properties:
      - url: https://www.w3.org/TR/wai-aria-1.2/
        type: Specification
      - url: https://www.w3.org/WAI/ARIA/
        type: Documentation
      - url: https://github.com/w3c/aria
        type: GitHub
  - aid: w3c:rdf
    name: RDF and SPARQL
    description: The Resource Description Framework (RDF) is a W3C standard for representing information in the web. RDF 1.2 and SPARQL 1.2 are the latest versions, providing the foundation for the semantic web and linked data. RDF triples express knowledge as subject-predicate-object relationships.
    humanURL: https://www.w3.org/RDF/
    tags:
      - Linked Data
      - RDF
      - Semantic Web
      - SPARQL
      - Standards
    properties:
      - url: https://www.w3.org/TR/rdf12-primer/
        type: Specification
      - url: https://www.w3.org/TR/sparql12-overview/
        type: SPARQL Specification
      - url: https://github.com/w3c/rdf-star-wg
        type: GitHub
  - aid: w3c:digital-credentials
    name: Digital Credentials API
    description: The W3C Digital Credentials API provides browser support for mediating presentation and issuance of digital credentials such as digital identity documents. It enables web applications to request and receive verifiable digital identity credentials from digital wallets in a privacy-preserving way.
    humanURL: https://www.w3.org/TR/digital-credentials/
    tags:
      - Credentials
      - Identity
      - Privacy
      - Security
      - Standards
    properties:
      - url: https://www.w3.org/TR/digital-credentials/
        type: Specification
      - url: https://github.com/w3c/digital-credentials
        type: GitHub
common:
  - url: https://www.w3.org/
    type: Website
  - url: https://www.w3.org/TR/
    type: TechnicalReports
  - url: https://api.w3.org/
    type: API
  - url: https://github.com/w3c/
    type: GitHubOrg
  - url: https://www.w3.org/news/
    type: News
  - url: https://www.w3.org/blog/
    type: Blog
  - url: https://www.w3.org/events/
    type: Events
  - url: https://www.w3.org/donate/
    type: Donations
  - url: https://w3c.social/@w3c
    type: Mastodon
  - url: https://www.linkedin.com/company/w3c/
    type: LinkedIn
  - url: https://www.youtube.com/@W3COfficial
    type: YouTube
  - url: https://www.w3.org/sponsor/
    type: Sponsorship
  - url: vocabulary/w3c-vocabulary.yml
    type: Vocabulary
  - url: json-ld/w3c-context.jsonld
    type: JSONLDContext
  - url: rules/w3c-rules.yml
    type: SpectralRules
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
