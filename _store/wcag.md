---
aid: wcag
name: WCAG
description: Web Content Accessibility Guidelines (WCAG) are a set of international standards published by the W3C Web Accessibility Initiative (WAI) for making web content accessible to people with disabilities. WCAG covers a wide range of recommendations across four principles (Perceivable, Operable, Understandable, Robust), with conformance levels A, AA, and AAA. WCAG 2.2 (ISO/IEC 40500:2025) is the current standard, while WCAG 3.0 is in active development targeting broader coverage of websites, mobile apps, VR environments, and digital documents.
type: Index
url: https://www.w3.org/WAI/standards-guidelines/wcag/
tags:
  - Accessibility
  - W3C
  - WCAG
  - Web Standards
  - Disability
  - Inclusive Design
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wcag:wcag-2-2
    name: WCAG 2.2
    description: 'Web Content Accessibility Guidelines 2.2, the current stable version and ISO/IEC 40500:2025 standard. Introduces 9 new success criteria beyond WCAG 2.1, including focus appearance, dragging movements, and consistent help. Organized into four principles: Perceivable, Operable, Understandable, and Robust (POUR).'
    humanURL: https://www.w3.org/TR/WCAG22/
    tags:
      - WCAG 2.2
      - Accessibility
      - Web Standards
      - ISO
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/WCAG22/
        title: WCAG 2.2 Specification
      - type: Documentation
        url: https://www.w3.org/WAI/WCAG22/quickref/
        title: WCAG 2.2 Quick Reference
      - type: Documentation
        url: https://github.com/w3c/wcag
        title: WCAG GitHub Repository
      - type: JSONSchema
        url: json-schema/wcag-success-criterion-schema.json
        title: Success Criterion Schema
      - type: JSONSchema
        url: json-schema/wcag-conformance-claim-schema.json
        title: Conformance Claim Schema
      - type: JSONStructure
        url: json-structure/wcag-success-criterion-structure.json
        title: Success Criterion Structure
      - type: JSONStructure
        url: json-structure/wcag-conformance-claim-structure.json
        title: Conformance Claim Structure
  - aid: wcag:wcag-3-0
    name: WCAG 3.0
    description: W3C Accessibility Guidelines 3.0 (working draft), expanding scope beyond web content to cover mobile apps, VR, authoring tools, and digital documents. Introduces outcome-based testing and a new scoring model. Working Draft published January 2026; Candidate Recommendation targeted Q4 2027.
    humanURL: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/
    tags:
      - WCAG 3.0
      - Accessibility
      - Web Standards
      - Working Draft
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/
        title: WCAG 3.0 Introduction
      - type: Documentation
        url: https://w3c.github.io/wcag3/guidelines/
        title: WCAG 3.0 Editor Draft
      - type: Documentation
        url: https://github.com/w3c/wcag3
        title: WCAG 3.0 GitHub Repository
  - aid: wcag:wai-aria
    name: WAI-ARIA
    description: Accessible Rich Internet Applications (WAI-ARIA) 1.2 specification providing semantic roles, states, and properties for accessible user interface components. Includes API mappings for browsers and assistive technologies.
    humanURL: https://www.w3.org/TR/wai-aria/
    tags:
      - WAI-ARIA
      - Accessibility
      - Semantic Web
      - User Interface
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/wai-aria/
        title: WAI-ARIA Specification
      - type: Documentation
        url: https://www.w3.org/TR/aria-in-html/
        title: ARIA in HTML
      - type: Documentation
        url: https://github.com/w3c/aria-practices
        title: ARIA Authoring Practices GitHub
  - aid: wcag:act-rules
    name: Accessibility Conformance Testing (ACT) Rules
    description: ACT Rules provide machine-executable rules for testing WCAG 2.x conformance, enabling consistent automated and manual accessibility evaluation across tools and methodologies.
    humanURL: https://www.w3.org/WAI/standards-guidelines/act/
    tags:
      - ACT Rules
      - Accessibility Testing
      - Automated Testing
      - WCAG
    properties:
      - type: Documentation
        url: https://www.w3.org/WAI/standards-guidelines/act/
        title: ACT Rules Overview
      - type: Documentation
        url: https://act-rules.github.io/
        title: ACT Rules Community
common:
  - type: Website
    url: https://www.w3.org/WAI/
    title: W3C Web Accessibility Initiative
  - type: Documentation
    url: https://www.w3.org/WAI/standards-guidelines/
    title: W3C Accessibility Standards Overview
  - type: GitHubOrganization
    url: https://github.com/w3c
    title: W3C GitHub Organization
  - type: Tools
    url: https://www.w3.org/WAI/test-evaluate/tools/list/
    title: Web Accessibility Evaluation Tools List
  - type: Tools
    url: https://github.com/w3c/wcag-em-report-tool
    title: WCAG-EM Report Tool
  - type: Vocabulary
    url: vocabulary/wcag-vocabulary.yml
    title: WCAG Vocabulary
  - type: JSON-LD
    url: json-ld/wcag-context.jsonld
    title: WCAG JSON-LD Context
  - type: Features
    data:
      - name: Four Accessibility Principles (POUR)
        description: 'WCAG 2.x guidelines are organized around four principles: Perceivable (information must be presentable to users), Operable (UI must be navigable), Understandable (content must be comprehensible), and Robust (content must be interpretable by assistive technologies).'
      - name: Three Conformance Levels
        description: Success criteria are classified as Level A (minimum), Level AA (standard), and Level AAA (enhanced), enabling graduated implementation roadmaps.
      - name: Testable Success Criteria
        description: Each guideline contains specific, testable success criteria that provide a clear pass/fail basis for accessibility evaluation and legal compliance.
      - name: ACT Rules Integration
        description: Machine-executable ACT Rules enable consistent automated testing of WCAG conformance across multiple evaluation tools.
      - name: Techniques and Failures Documentation
        description: Extensive documentation of sufficient techniques, advisory techniques, and common failures for implementing and evaluating each success criterion.
      - name: WCAG 3.0 Outcome-Based Model
        description: WCAG 3.0 introduces a scoring-based conformance model with outcomes replacing binary pass/fail for more nuanced accessibility assessment.
  - type: UseCases
    data:
      - name: Legal Compliance
        description: Organizations use WCAG 2.1/2.2 Level AA to meet legal accessibility requirements including ADA, Section 508, EN 301 549, and AODA.
      - name: Automated Accessibility Testing
        description: Development teams integrate ACT Rules into CI/CD pipelines to automatically catch WCAG violations in web applications.
      - name: Screen Reader Compatibility
        description: WAI-ARIA roles and properties enable web applications to communicate semantic structure and state to screen readers and assistive technologies.
      - name: Accessibility Auditing
        description: Accessibility specialists use WCAG criteria as the evaluation framework for manual and automated accessibility audits.
      - name: Inclusive Design
        description: Design and engineering teams reference WCAG guidelines during the design phase to build accessibility in from the start rather than retrofitting.
  - type: Integrations
    data:
      - name: axe-core
        description: Popular open-source accessibility testing engine that maps test rules to WCAG success criteria.
      - name: WAVE
        description: Web Accessibility Evaluation Tool that visually highlights WCAG issues on web pages.
      - name: Lighthouse
        description: Google Lighthouse includes accessibility audits mapped to WCAG criteria.
      - name: NVDA and JAWS
        description: Screen readers that implement WAI-ARIA API mappings to communicate accessible rich web content to blind and low-vision users.
      - name: ISO/IEC 40500
        description: WCAG 2.2 is identical to ISO/IEC 40500:2025, enabling reference in international procurement and regulatory requirements.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
