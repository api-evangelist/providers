---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apple Keynote Agentic Access
  operation_count: 11
  slug: apple-keynote-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 7
apis:
- description: Local automation API for Keynote using AppleScript, enabling programmatic control of presentations, slides, and elements on macOS. Access via the Open Scripting Architecture dictionary.
  name: Keynote AppleScript API
  slug: keynote-applescript-api
- description: JavaScript-based automation interface for controlling Keynote on macOS using the Open Scripting Architecture (OSA). Provides the same capabilities as AppleScript using JavaScript syntax via JXA.
  name: Keynote JavaScript for Automation API
  slug: keynote-javascript-for-automation-api
- description: Shortcuts app actions for Keynote on iOS, iPadOS, and macOS, enabling users to open, create, and export presentations as part of automated workflows including format conversion and template generation
  name: Keynote Shortcuts Actions
  slug: keynote-shortcuts-actions
- description: Exporting presentations to various formats
  name: Apple Keynote Export API
  slug: apple-keynote-export-api
- description: Keynote presentation document management
  name: Apple Keynote Presentations API
  slug: apple-keynote-presentations-api
- description: Slide operations within a presentation
  name: Apple Keynote Slides API
  slug: apple-keynote-slides-api
- description: Presentation themes and templates
  name: Apple Keynote Themes API
  slug: apple-keynote-themes-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apple Keynote iCloud Export API
  slug: open-apple-keynote-export-api
- collection_type: open
  name: Apple Keynote iCloud Export Presentations API
  slug: open-apple-keynote-presentations-api
- collection_type: open
  name: Apple Keynote iCloud Export Slides API
  slug: open-apple-keynote-slides-api
- collection_type: open
  name: Apple Keynote iCloud Export Themes API
  slug: open-apple-keynote-themes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apple-keynote-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apple-keynote-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apple-keynote-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.apple.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.apple.com/guide/keynote/
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.apple.com/support/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/privacy/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/keynote
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AppleDeveloper
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apple-keynote-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/apple-keynote-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apple-keynote-vocabulary.yaml
created: '2024-01-01'
description: Apple Keynote is a presentation software application developed by Apple Inc. as part of the iWork productivity suite, available on macOS, iOS, iPadOS, and the web via iCloud. It enables creating visually rich presentations with animations, transitions, charts, and real-time collaboration. Keynote supports automation via AppleScript, JavaScript for Automation (JXA), and Apple Shortcuts, and provides iCloud-based access for cross-device sync and sharing.
examples:
- key_count: 3
  name: Apple Keynote Export Request Example
  slug: apple-keynote-export-request-example
- key_count: 8
  name: Apple Keynote Presentation Example
  slug: apple-keynote-presentation-example
- key_count: 6
  name: Apple Keynote Slide Example
  slug: apple-keynote-slide-example
- key_count: 5
  name: Apple Keynote Theme Example
  slug: apple-keynote-theme-example
features:
- description: Available on macOS, iOS, iPadOS, and web browsers via iCloud
  name: Multi-Platform Availability
- description: Multiple users can edit presentations simultaneously via iCloud sharing
  name: Real-Time Collaboration
- description: Intelligent morph transitions that animate elements between slides
  name: Magic Move Transitions
- description: Full scripting support via AppleScript and JavaScript for Automation
  name: AppleScript Automation
- description: Apple Shortcuts actions for automated presentation workflows on iOS and macOS
  name: Shortcuts Integration
- description: Export to PDF, PowerPoint (.pptx), HTML, images, and native .key format
  name: Multi-Format Export
- description: Present with live video overlays in video conferencing applications
  name: Live Video Presenter
- description: Rich build-in and build-out animations for slide elements
  name: Cinematic Animations
- description: Built-in chart types including bar, line, pie, scatter, and more with live data
  name: Charts and Data Visualization
finops:
- name: Apple Keynote Finops
  service_category: Productivity / Presentations
  slug: apple-keynote-finops
image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
json_schemas:
- name: ExportRequest
  property_count: 3
  slug: apple-keynote-export-request
- name: Apple Keynote Presentation
  property_count: 9
  slug: apple-keynote-presentation
- name: Slide
  property_count: 6
  slug: apple-keynote-slide
- name: Theme
  property_count: 5
  slug: apple-keynote-theme
json_structures:
- name: Apple Keynote Export Request Structure
  property_count: 3
  slug: apple-keynote-export-request-structure
- name: Apple Keynote Presentation Structure
  property_count: 9
  slug: apple-keynote-presentation-structure
- name: Apple Keynote Slide Structure
  property_count: 6
  slug: apple-keynote-slide-structure
- name: Apple Keynote Theme Structure
  property_count: 5
  slug: apple-keynote-theme-structure
jsonld:
- class_count: 9
  name: Apple Keynote Context
  property_count: 17
  slug: apple-keynote-context
layout: provider
modified: '2026-05-19'
name: Apple Keynote
nav: Providers
network: true
overview: 'Apple Keynote publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Export API, Presentations API, Slides API, and 1 more. Tagged areas include Apple, Design, iWork, Presentations, and Productivity.


  The Apple Keynote catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apple Keynote''s developer surface includes developer portal, documentation, support, Stack Overflow tag, YouTube channel, and 8 more developer resources.'
plans:
- name: Apple Keynote Plans Pricing
  plan_count: 7
  slug: apple-keynote-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Apple Keynote Rate Limits
  slug: apple-keynote-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Apple Keynote API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: apple-keynote-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Apple Keynote API Rules
  rule_count: 27
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 17
  slug: apple-keynote-spectral-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 30.0
    developer_ergonomics: 31.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apple-keynote/refs/heads/main/screenshots/apple-keynote-2026-06-20T172318.png
security:
- kind: domain-security
  name: Apple Keynote Domain Security
  slug: apple-keynote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Keynote Vulnerability Disclosure
  slug: apple-keynote-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apple-keynote
tags:
- Apple
- Design
- iWork
- Presentations
- Productivity
- Slides
use_cases:
- description: Creating professional pitch decks, board presentations, and quarterly reviews
  name: Business Presentations
- description: Designing lecture slides, course materials, and educational presentations
  name: Educational Content
- description: Producing brand presentations, product launches, and sales decks
  name: Marketing Materials
- description: Using AppleScript or Shortcuts to programmatically generate recurring presentation reports
  name: Automated Report Generation
- description: Creating polished conference talks with animations and transitions
  name: Conference Presentations
- description: Building step-by-step training and onboarding presentations
  name: Training Materials
website: https://developer.apple.com/
---
