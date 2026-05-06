---
aid: accessibility-standards
url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/apis.yml
name: Accessibility Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accessibility
  - Compliance
  - UX
  - Web Standards
  - WCAG
  - ARIA
  - Section 508
  - Disability
description: Guidelines and technical specifications that ensure digital content, applications, and technologies are usable by people with disabilities, including standards like WCAG, Section 508, and ARIA. These standards help organizations meet regulatory requirements and demonstrate accountability to stakeholders.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: Web Content Accessibility Guidelines (WCAG) 2.2
    description: 'The current stable web accessibility standard published by the W3C Accessibility Guidelines Working Group (AG WG). WCAG 2.2 comprises 13 guidelines organized under four principles (perceivable, operable, understandable, robust) with success criteria at three levels: A, AA, and AAA. It has been adopted as ISO/IEC 40500:2025 and is referenced by Section 508 and the EU Accessibility Act.'
    humanURL: https://www.w3.org/WAI/standards-guidelines/wcag/
    baseURL: https://www.w3.org/TR/WCAG22/
    tags:
      - WCAG
      - Web Content
      - Accessibility
      - W3C
      - ISO
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/wcag/
      - type: Specification
        url: https://www.w3.org/TR/WCAG22/
      - type: Documentation
        url: https://www.w3.org/WAI/WCAG22/quickref/
        title: WCAG 2.2 Quick Reference
      - type: GitHubRepository
        url: https://github.com/w3c/wcag
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-schema/wcag-success-criterion-schema.json
        title: WCAG Success Criterion Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-schema/wcag-conformance-report-schema.json
        title: WCAG Conformance Report Schema
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-structure/wcag-success-criterion-structure.json
        title: WCAG Success Criterion Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-structure/wcag-conformance-report-structure.json
        title: WCAG Conformance Report Structure
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/examples/wcag-success-criterion-example.json
        title: WCAG Success Criterion Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/examples/wcag-conformance-report-example.json
        title: WCAG Conformance Report Example
  - name: WAI-ARIA 1.2
    description: Accessible Rich Internet Applications (WAI-ARIA) 1.2 is a W3C Recommendation (June 2023) that defines semantic attributes enabling assistive technologies to interpret dynamic web content and complex interfaces. The suite includes Core Accessibility API Mappings, Accessible Name and Description Computation, and HTML/SVG API Mappings.
    humanURL: https://www.w3.org/WAI/standards-guidelines/aria/
    baseURL: https://www.w3.org/TR/wai-aria-1.2/
    tags:
      - ARIA
      - Semantic
      - Screen Reader
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/aria/
      - type: Specification
        url: https://www.w3.org/TR/wai-aria-1.2/
      - type: Documentation
        url: https://www.w3.org/WAI/ARIA/apg/
        title: ARIA Authoring Practices Guide
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-schema/aria-role-schema.json
        title: ARIA Role Schema
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-structure/aria-role-structure.json
        title: ARIA Role Structure
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/examples/aria-role-example.json
        title: ARIA Role Example
  - name: Authoring Tool Accessibility Guidelines (ATAG) 2.0
    description: ATAG 2.0 is a W3C Recommendation that defines standards for making authoring tools (CMSes, code editors, web-based tools) accessible to authors with disabilities, and for helping those tools generate accessible content.
    humanURL: https://www.w3.org/WAI/standards-guidelines/atag/
    baseURL: https://www.w3.org/TR/ATAG/
    tags:
      - ATAG
      - Authoring Tools
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/atag/
      - type: Specification
        url: https://www.w3.org/TR/ATAG/
  - name: User Agent Accessibility Guidelines (UAAG) 2.0
    description: UAAG 2.0 is a W3C standard for browsers, browser extensions, media players, and other user agents that render web content. It defines how user agents should make web content accessible to users with disabilities either directly or in conjunction with assistive technologies.
    humanURL: https://www.w3.org/WAI/standards-guidelines/uaag/
    baseURL: https://www.w3.org/TR/UAAG20/
    tags:
      - UAAG
      - Browsers
      - User Agents
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/uaag/
      - type: Specification
        url: https://www.w3.org/TR/UAAG20/
  - name: Section 508
    description: Section 508 of the Rehabilitation Act requires U.S. federal agencies to ensure their information and communication technology (ICT) is accessible to people with disabilities. The Revised 508 Standards (effective January 18, 2017) incorporate WCAG 2.0 Level A and AA success criteria for web and electronic content across seven chapters of requirements.
    humanURL: https://www.access-board.gov/ict/
    baseURL: https://www.section508.gov/
    tags:
      - Section 508
      - Federal
      - Government
      - US Law
      - ICT
    properties:
      - type: Documentation
        url: https://www.access-board.gov/ict/
      - type: Documentation
        url: https://www.section508.gov/develop/web-content/
        title: Section 508 Web Content Development Guidance
  - name: Accessibility Conformance Testing (ACT) Rules Format 1.1
    description: ACT Rules Format 1.1 (W3C Recommendation, February 2026) establishes a standardized format for documenting accessibility conformance testing rules. The framework supports automated, semi-automated, and manual testing and is used to create transparent, interoperable accessibility testing methodologies aligned with WCAG.
    humanURL: https://www.w3.org/WAI/standards-guidelines/act/
    baseURL: https://www.w3.org/TR/act-rules-format/
    tags:
      - ACT
      - Testing
      - Conformance
      - W3C
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/act/
      - type: Specification
        url: https://www.w3.org/TR/act-rules-format/
      - type: GitHubRepository
        url: https://github.com/w3c/wcag-act-rules
        title: WCAG ACT Rules Repository
common:
  - type: Website
    url: https://www.w3.org/WAI/standards-guidelines/
  - type: GitHubOrganization
    url: https://github.com/w3c
    title: W3C GitHub Organization
  - type: Tools
    url: https://www.w3.org/WAI/test-evaluate/tools/list/
    title: W3C Accessibility Evaluation Tools List
  - type: Tools
    url: https://github.com/dequelabs/axe-core
    title: axe-core Accessibility Testing Engine
  - type: Tools
    url: https://github.com/pa11y/pa11y
    title: Pa11y Automated Accessibility Testing
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/json-ld/accessibility-standards-context.jsonld
    title: Accessibility Standards JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/accessibility-standards/refs/heads/main/vocabulary/accessibility-standards-vocabulary.yaml
    title: Accessibility Standards Vocabulary
  - type: Features
    data:
      - name: Perceivable Content
        description: Standards requiring that information and user interface components be presentable to users in ways they can perceive, including text alternatives for non-text content.
      - name: Operable Interface
        description: Standards ensuring that user interface components and navigation are operable, including keyboard accessibility and sufficient time limits.
      - name: Understandable Information
        description: Standards ensuring that information and the operation of the user interface is understandable, including readable text and predictable navigation.
      - name: Robust Technology
        description: Standards requiring that content be robust enough to be reliably interpreted by a wide variety of user agents, including assistive technologies.
      - name: Conformance Levels
        description: Three-tiered conformance model (Level A, AA, AAA) providing graduated accessibility requirements for organizations to target.
      - name: Automated Testing Rules
        description: ACT Rules Framework providing standardized, machine-readable rules for automated accessibility conformance testing.
  - type: UseCases
    data:
      - name: Web Application Accessibility Auditing
        description: Using WCAG 2.2 success criteria and ACT rules to audit web applications for accessibility compliance.
      - name: Federal Government ICT Procurement
        description: Applying Section 508 standards when procuring or developing information and communication technology for U.S. federal agencies.
      - name: Accessible Rich Internet Application Development
        description: Using WAI-ARIA attributes to make dynamic JavaScript-driven interfaces accessible to screen readers and assistive technologies.
      - name: Automated CI/CD Accessibility Testing
        description: Integrating axe-core or Pa11y into continuous integration pipelines to catch accessibility regressions automatically.
      - name: Regulatory Compliance Documentation
        description: Producing Voluntary Product Accessibility Templates (VPATs) and Accessibility Conformance Reports aligned with Section 508 and WCAG.
  - type: Integrations
    data:
      - name: axe-core
        description: Open-source accessibility testing engine by Deque Systems implementing WCAG 2.0/2.1/2.2 rules, integrates with browsers, testing frameworks, and CI tools.
      - name: Pa11y
        description: Open-source Node.js tool for automated accessibility testing against WCAG standards, integrates with GitHub Actions and CI/CD pipelines.
      - name: Section508.gov
        description: GSA's Government-wide IT Accessibility Program providing guidance, training, and resources for federal Section 508 compliance.
      - name: EU Accessibility Act / EN 301 549
        description: European standard referencing WCAG 2.1 AA, applicable to public and private sector digital services in EU member states.
      - name: ISO/IEC 40500:2025
        description: International Standards Organization adoption of WCAG 2.2, enabling global regulatory alignment with the W3C standard.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
