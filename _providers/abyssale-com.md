---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Abyssale Com Agentic Access
  operation_count: 23
  slug: abyssale-com-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Auth API from Abyssale — 1 operation(s) for auth.
  name: Abyssale Auth API
  slug: abyssale-com-auth-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Credits API from Abyssale — 1 operation(s) for credits.
  name: Abyssale Credits API
  slug: abyssale-com-credits-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Design Duplication Requests API from Abyssale — 1 operation(s) for design duplication requests.
  name: Abyssale Design Duplication Requests API
  slug: abyssale-com-design-duplication-requests-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Designs API from Abyssale — 10 operation(s) for designs.
  name: Abyssale Designs API
  slug: abyssale-com-designs-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Examples API from Abyssale — 1 operation(s) for examples.
  name: Abyssale Examples API
  slug: abyssale-com-examples-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Export Abyssale API from Abyssale — 1 operation(s) for export abyssale.
  name: Abyssale Export Abyssale API
  slug: abyssale-com-export-abyssale-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Fonts API from Abyssale — 1 operation(s) for fonts.
  name: Abyssale Fonts API
  slug: abyssale-com-fonts-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Images API from Abyssale — 1 operation(s) for images.
  name: Abyssale Images API
  slug: abyssale-com-images-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Projects API from Abyssale — 1 operation(s) for projects.
  name: Abyssale Projects API
  slug: abyssale-com-projects-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Workspace Template Categories API from Abyssale — 1 operation(s) for workspace template categories.
  name: Abyssale Workspace Template Categories API
  slug: abyssale-com-workspace-template-categories-api
- baseURL: https://api.abyssale.com
  baseurl_source: declared
  description: The Workspace Templates API from Abyssale — 2 operation(s) for workspace templates.
  name: Abyssale Workspace Templates API
  slug: abyssale-com-workspace-templates-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/abyssale-com/agentic-access/abyssale-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abyssale-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/abyssale-com/rules/abyssale-com-rules.yml
  title: ''
  type: Spectral
  url: rules/abyssale-com-rules.yml
- group: design
  href: https://artifacts.apis.io/abyssale-com/json-ld/abyssale-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/abyssale-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/abyssale-com/vocabulary/abyssale-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abyssale-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/abyssale-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/abyssale-com/data-model/abyssale-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abyssale-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/abyssale-com/conformance/abyssale-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abyssale-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abyssale-com/llms/abyssale-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abyssale-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/abyssale-com/well-known/abyssale-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abyssale-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/abyssale-com/well-known/abyssale-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abyssale-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/abyssale-com/hosts/abyssale-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abyssale-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/abyssale-com/vendors/abyssale-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abyssale-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.abyssale.com/register
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@abyssale/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.abyssale.com/mcp/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.abyssale.com/rest-api/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.abyssale.com</code
- group: auth
  href: https://artifacts.apis.io/abyssale-com/authentication/abyssale-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abyssale-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/abyssale-com/security/abyssale-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abyssale-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abyssale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.abyssale.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.abyssale.com/api-reference/
- group: operate
  title: ''
  type: Support
  url: https://help.abyssale.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.abyssale.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.abyssale.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abyssale.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abyssale.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getabyssale
created: '2026-10-31'
description: Abyssale is a creative automation platform founded in 2019 in Paris, France. It helps agencies and marketing teams scale visual production by generating on‑brand images, videos, PDFs and HTML5 ads from templates. The service offers dynamic image URLs, webhooks, and SDKs for Node.js and Python, enabling rapid creation of marketing assets at scale.
image: https://cdn.prod.website-files.com/672b6e17b837fe6d8ed6a300/6786ac25c08789ffad3c3b1c_Webclip.png
json_schemas:
- name: GetDesignDuplicationRequestsDuplicaterequestidResponse
  property_count: 7
  slug: abyssale-com-get-design-duplication-requests-duplicaterequestid-response
- name: GetDesignsDesignidFormatsFacebookPostResponse
  property_count: 9
  slug: abyssale-com-get-designs-designid-formats-facebook-post-response
- name: GetDesignsImportJson64238D01D402474B8C2DFbc957E9D290Response
  property_count: 8
  slug: abyssale-com-get-designs-import-json64238-d01-d402474-b8-c2-dfbc957-e9-d290-response
- name: GetWorkspaceTemplatesResponse
  property_count: 8
  slug: abyssale-com-get-workspace-templates-response
- name: PostDesignsDesignidDynamicImageUrlResponse
  property_count: 3
  slug: abyssale-com-post-designs-designid-dynamic-image-url-response
- name: PostImagesRequest
  property_count: 3
  slug: abyssale-com-post-images-request
jsonld:
- class_count: 20
  name: Abyssale Com Context
  property_count: 43
  slug: abyssale-com-context
layout: provider
modified: '2026-10-31'
name: Abyssale
nav: Providers
network: true
overview: 'Abyssale publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Credits API, Design Duplication Requests API, and 8 more. Tagged areas include Creative Automation, Marketing, Agencies, Visual-Production, and Software-as-a-Service.


  The Abyssale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Abyssale''s developer surface includes signup flow, changelog, getting-started guide, authentication, documentation, API reference, support, and 21 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Abyssale API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: abyssale-com-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 48.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Abyssale Com Authentication
  slug: abyssale-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abyssale Com Domain Security
  slug: abyssale-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: design-management
  slug: abyssale-com-design-management
slug: abyssale-com
tags:
- Creative Automation
- Marketing
- Agencies
- Visual-Production
- Software-as-a-Service
website: https://www.abyssale.com/
---
