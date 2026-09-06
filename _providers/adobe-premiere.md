---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Adobe Premiere Agentic Access
  operation_count: 10
  slug: adobe-premiere-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: Adobe Premiere Pro extension APIs using UXP (Unified Extensibility Platform) and CEP (Common Extensibility Platform) for building plugins and panels that automate video editing workflows, add custom e
  name: Adobe Premiere Pro API
  slug: adobe-premiere-pro-api
- baseURL: https://cc-libraries.adobe.io
  baseurl_source: declared
  description: Manage library elements (colors, graphics, fonts, etc.)
  name: Adobe Premiere Pro Elements API
  slug: adobe-premiere-elements-api
- baseURL: https://cc-libraries.adobe.io
  baseurl_source: declared
  description: Manage Creative Cloud Libraries
  name: Adobe Premiere Pro Libraries API
  slug: adobe-premiere-libraries-api
- baseURL: https://cc-libraries.adobe.io
  baseurl_source: declared
  description: Manage element representations and renditions
  name: Adobe Premiere Pro Representations API
  slug: adobe-premiere-representations-api
- baseURL: https://cc-libraries.adobe.io
  baseurl_source: declared
  description: Adobe's published REST API for Creative Cloud Libraries — the shared asset store (colors, character styles, brushes, graphics, patterns and video) that Premiere Pro panels read and write. 25 operation
  name: Adobe Creative Cloud Libraries API
  slug: adobe-creative-cloud-libraries-api
arazzos:
- description: Create a library, add an element to it, then read the element back.
  name: Adobe Premiere Add Element to Creative Cloud Library
  slug: adobe-premiere-add-element-to-library-workflow
- description: Resolve a library then list a page of its elements.
  name: Adobe Premiere Catalog Creative Cloud Library Elements
  slug: adobe-premiere-catalog-library-elements-workflow
- description: Resolve an element then fetch one of its representations by id.
  name: Adobe Premiere Fetch Library Element Representation
  slug: adobe-premiere-fetch-element-representation-workflow
- description: Search libraries by name and reuse the match, or create one when none exists.
  name: Adobe Premiere Find or Create Creative Cloud Library
  slug: adobe-premiere-find-or-create-library-workflow
- description: Create a Creative Cloud Library and read it back to confirm it exists.
  name: Adobe Premiere Provision Creative Cloud Library
  slug: adobe-premiere-provision-library-workflow
- description: List a library's elements, delete the first one, then delete the library.
  name: Adobe Premiere Purge Creative Cloud Library
  slug: adobe-premiere-purge-library-workflow
- description: Read a library, update its name, then read it back to confirm the change.
  name: Adobe Premiere Rename and Verify Creative Cloud Library
  slug: adobe-premiere-rename-and-verify-library-workflow
artifact_total: 73
asyncapis:
- description: ''
  name: Adobe Premiere Libraries Webhooks
  slug: adobe-premiere-libraries-webhooks
collections:
- collection_type: postman
  name: Adobe Creative Cloud Libraries API
  slug: postman-adobe-premiere-creative-cloud-libraries
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Creative Cloud Libraries API
  slug: open-adobe-premiere-creative-cloud-libraries
- collection_type: open
  name: Adobe Creative Cloud Libraries Elements API
  slug: open-adobe-premiere-elements-api
- collection_type: open
  name: Adobe Creative Cloud Elements Libraries API
  slug: open-adobe-premiere-libraries-api
- collection_type: open
  name: Adobe Creative Cloud Libraries Elements Representations API
  slug: open-adobe-premiere-representations-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/products/premiere.html
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-premiere-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-premiere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-premiere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-premiere-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adobe-premiere-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-premiere-pro/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-add-element-to-library-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-catalog-library-elements-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-fetch-element-representation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-find-or-create-library-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-provision-library-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-purge-library-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-premiere-rename-and-verify-library-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobepremierepro
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/premiere-pro/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/premiere-pro/uxp/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/support/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/AdobeDevelopers
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/premiere-pro/uxp/introduction/
- group: design
  title: ''
  type: SpectralRules
  url: rules/adobe-premiere-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-premiere-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/adobe-premiere-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adobe-premiere-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adobe-premiere-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adobe-premiere-security.txt
- group: auth
  title: ''
  type: Security
  url: security/adobe-premiere-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/adobe-premiere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adobe-premiere-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/adobe-premiere-cc-libraries-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/adobe-premiere-elements-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/adobe-premiere-libraries-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/adobe-premiere-representations-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/adobe-premiere-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adobe-premiere-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-premiere-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adobe-premiere-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adobe-premiere-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adobe-premiere-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adobe-premiere-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adobe-premiere-libraries-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adobe-premiere-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adobe-premiere-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adobe.com/premiere-pro/uxp/ppro-reference/
- group: start
  title: ''
  type: Quickstart
  url: https://developer.adobe.com/premiere-pro/uxp/plugins/tutorials/
- group: operate
  title: ''
  type: HelpCenter
  url: https://forums.creativeclouddeveloper.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-premiere-creative-cloud-libraries-context.jsonld
created: '2024-01-01'
description: 'Adobe Premiere Pro is a professional non-linear video editor. Its programmable surface has two halves: the Premiere UXP API, an in-process JavaScript DOM for plugins and panels that automate editing, extend the timeline and integrate hardware or media asset management systems inside the desktop application; and the Adobe Creative Cloud Libraries REST API on cc-libraries.adobe.io, which is what a Premiere panel calls over HTTP to read and write shared assets — colors, character styles, graphics, patterns and video — along with an Adobe I/O Events webhook surface for library changes.'
examples:
- key_count: 6
  name: Creative Cloud Libraries Element Example
  slug: creative-cloud-libraries-element-example
- key_count: 2
  name: Creative Cloud Libraries Element Input Example
  slug: creative-cloud-libraries-element-input-example
- key_count: 4
  name: Creative Cloud Libraries Element List Example
  slug: creative-cloud-libraries-element-list-example
- key_count: 6
  name: Creative Cloud Libraries Library Example
  slug: creative-cloud-libraries-library-example
- key_count: 1
  name: Creative Cloud Libraries Library Input Example
  slug: creative-cloud-libraries-library-input-example
- key_count: 4
  name: Creative Cloud Libraries Library List Example
  slug: creative-cloud-libraries-library-list-example
- key_count: 1
  name: Creative Cloud Libraries Links Example
  slug: creative-cloud-libraries-links-example
- key_count: 3
  name: Creative Cloud Libraries Representation Example
  slug: creative-cloud-libraries-representation-example
features:
- description: Build next-generation Premiere Pro plugins using the Unified Extensibility Platform (UXP) with modern HTML, CSS, and JavaScript.
  name: UXP Plugin Development
- description: Create custom workspace panels using Common Extensibility Platform (CEP) with HTML, CSS, and JavaScript for legacy support.
  name: CEP Panel Integration
- description: Build powerful low-level integrations with codec support, custom effects, and hardware communication using the C++ SDK.
  name: C++ SDK Extensions
- description: Programmatically access and manage shared design assets including colors, graphics, fonts, and video via REST API.
  name: Creative Cloud Libraries Access
- description: Automate complex video editing tasks, batch processing, and project management within Premiere Pro.
  name: Workflow Automation
- description: Integrate Premiere Pro with external media asset management systems, hardware controllers, and cloud services.
  name: Third-Party Integration
finops:
- name: Adobe Premiere Finops
  service_category: API
  slug: adobe-premiere-finops
image: /assets/icons/adobe-premiere.png
integrations:
- description: Deep integration with After Effects for motion graphics and VFX roundtrip workflows via Dynamic Link.
  name: Adobe After Effects
- description: Send audio clips and sequences to Audition for advanced audio editing and roundtrip import.
  name: Adobe Audition
- description: Real-time collaboration and review workflows integrated directly into Premiere Pro via Frame.io panel.
  name: Frame.io
- description: Visual effects and motion graphics plugins including Sapphire, Continuum, and Mocha Pro.
  name: Boris FX
- description: Motion graphics and 3D rendering integration for titles and compositing.
  name: Maxon Cinema 4D
- description: AAF and project interchange for cross-platform editorial workflows.
  name: Avid Media Composer
- description: Cross-cloud file sharing and collaboration for media asset management.
  name: Iconik
json_schemas:
- name: ElementInput
  property_count: 2
  slug: creative-cloud-libraries-element-input
- name: ElementList
  property_count: 4
  slug: creative-cloud-libraries-element-list
- name: Element
  property_count: 6
  slug: creative-cloud-libraries-element
- name: LibraryInput
  property_count: 1
  slug: creative-cloud-libraries-library-input
- name: LibraryList
  property_count: 4
  slug: creative-cloud-libraries-library-list
- name: Library
  property_count: 6
  slug: creative-cloud-libraries-library
- name: Links
  property_count: 1
  slug: creative-cloud-libraries-links
- name: Representation
  property_count: 3
  slug: creative-cloud-libraries-representation
json_structures:
- name: Creative Cloud Libraries Element Input Structure
  property_count: 2
  slug: creative-cloud-libraries-element-input-structure
- name: Creative Cloud Libraries Element List Structure
  property_count: 4
  slug: creative-cloud-libraries-element-list-structure
- name: Creative Cloud Libraries Element Structure
  property_count: 6
  slug: creative-cloud-libraries-element-structure
- name: Creative Cloud Libraries Library Input Structure
  property_count: 1
  slug: creative-cloud-libraries-library-input-structure
- name: Creative Cloud Libraries Library List Structure
  property_count: 4
  slug: creative-cloud-libraries-library-list-structure
- name: Creative Cloud Libraries Library Structure
  property_count: 6
  slug: creative-cloud-libraries-library-structure
- name: Creative Cloud Libraries Links Structure
  property_count: 1
  slug: creative-cloud-libraries-links-structure
- name: Creative Cloud Libraries Representation Structure
  property_count: 3
  slug: creative-cloud-libraries-representation-structure
jsonld:
- class_count: 11
  name: Adobe Premiere Creative Cloud Libraries Context
  property_count: 12
  slug: adobe-premiere-creative-cloud-libraries-context
layout: provider
modified: '2026-04-19'
name: Adobe Premiere Pro
nav: Providers
network: true
overview: 'Adobe Premiere Pro publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Elements API, Libraries API, Representations API, and 1 more. Tagged areas include Adobe, Automation, Creative Cloud, Media, and Premiere Pro.


  The Adobe Premiere Pro catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Adobe Premiere Pro''s developer surface includes authentication, developer portal, documentation, engineering blog, support, developer console, YouTube channel, and 47 more developer resources.'
plans:
- name: Adobe Premiere Plans Pricing
  plan_count: 0
  slug: adobe-premiere-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Adobe Premiere Rate Limits
  slug: adobe-premiere-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Adobe Premiere Pro API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: adobe-premiere-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Adobe Premiere Pro API Rules
  rule_count: 33
  severity_counts:
    error: 16
    hint: 0
    info: 0
    warn: 17
  slug: adobe-premiere-spectral-rules
scopes:
- name: Adobe Premiere Scopes
  scope_count: 4
  slug: adobe-premiere-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 47.0
    contract_quality: 79.2
    developer_ergonomics: 74.4
    discoverability: 68.5
    governance: 47.0
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-premiere/refs/heads/main/screenshots/adobe-premiere-2026-06-20T165010.png
security:
- kind: authentication
  name: Adobe Premiere Authentication
  slug: adobe-premiere-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Adobe Premiere Domain Security
  slug: adobe-premiere-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Premiere Vulnerability Disclosure
  slug: adobe-premiere-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-premiere
tags:
- Adobe
- Automation
- Creative Cloud
- Media
- Premiere Pro
- Video Editing
- Video Production
use_cases:
- description: Build plugins that automatically generate and insert captions into video timelines using speech-to-text APIs.
  name: Automated Caption Generation
- description: Connect Premiere Pro to MAM systems for automated ingest, proxy workflows, and metadata management.
  name: Media Asset Management Integration
- description: Create workspace panels that surface brand-approved assets from Creative Cloud Libraries directly in Premiere Pro.
  name: Custom Branding Panel
- description: Automate batch export of sequences to multiple formats and destinations using CEP scripting.
  name: Batch Video Export
- description: Integrate AI/ML services for automatic cut detection, scene analysis, and intelligent timeline assembly.
  name: AI-Powered Editing
- description: Connect editing consoles, color grading hardware, and custom input devices to Premiere Pro workflows.
  name: Hardware Controller Integration
website: https://www.adobe.com/products/premiere.html
---
