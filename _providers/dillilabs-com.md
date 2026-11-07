---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dillilabs Com Agentic Access
  operation_count: 5
  slug: dillilabs-com-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 2
apis:
- description: Validates an email address; documented usage is GET https://deva.dillilabs.com/api/{API_KEY}/email/{address}?ip={IP_ADDRESS}, returning true if valid and false if invalid. Also published as a remote M
  name: Dilli Email Validation API (DEVA)
  slug: dilli-email-validation-api-deva
- description: Returns the ISO alpha-2 country code and country name for an IP address; documented usage is GET https://api.dillilabs.com/dil/<API_KEY>/ip/IP_ADDRESS.
  name: Dilli IP Geolocation API (DIL)
  slug: dilli-ip-geolocation-api-dil
- description: Checks an IP address against abuse blacklists; documented usage is GET https://api.dillilabs.com/diva/<API_KEY>/ip/IP_ADDRESS, returning 404 if clean or 200 with the blacklisting source if known to ab
  name: Dilli IP Address Validation API (DIVA)
  slug: dilli-ip-address-validation-api-diva
- description: Checks a string of text for profanity; documented usage is POST https://api.dillilabs.com/devil/{API_KEY} with a text parameter, returning true if it contains profanity and false if clean.
  name: Dilli Profanity Detection API (DeVIL)
  slug: dilli-profanity-detection-api-devil
- baseURL: https://mindyourtongue.dillilabs.com
  baseurl_source: declared
  description: The Analyze API from Dilli Labs — 1 operation(s) for analyze.
  name: Dilli Labs Analyze API
  slug: dillilabs-com-analyze-api
- baseURL: https://mindyourtongue.dillilabs.com
  baseurl_source: declared
  description: The Health API from Dilli Labs — 1 operation(s) for health.
  name: Dilli Labs Health API
  slug: dillilabs-com-health-api
- baseURL: https://mindyourtongue.dillilabs.com
  baseurl_source: declared
  description: The Privacy API from Dilli Labs — 1 operation(s) for privacy.
  name: Dilli Labs Privacy API
  slug: dillilabs-com-privacy-api
- baseURL: https://mindyourtongue.dillilabs.com
  baseurl_source: declared
  description: The Purchase API from Dilli Labs — 1 operation(s) for purchase.
  name: Dilli Labs Purchase API
  slug: dillilabs-com-purchase-api
- baseURL: https://mindyourtongue.dillilabs.com
  baseurl_source: declared
  description: The User API from Dilli Labs — 1 operation(s) for user.
  name: Dilli Labs User API
  slug: dillilabs-com-user-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/dillilabs-com/agentic-access/dillilabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dillilabs-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dillilabs-com/plans/dillilabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dillilabs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/rules/dillilabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dillilabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/json-ld/dillilabs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dillilabs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dillilabs-com/vocabulary/dillilabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dillilabs-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dillilabs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/data-model/dillilabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dillilabs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/conventions/dillilabs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dillilabs-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dillilabs-com/authentication/dillilabs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dillilabs-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/errors/dillilabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dillilabs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dillilabs-com/conformance/dillilabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dillilabs-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dillilabs-com/overlays/dillilabs-com-mind-your-tongue-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dillilabs-com-mind-your-tongue-overlay.yaml
- group: build
  href: https://artifacts.apis.io/dillilabs-com/mcp/dillilabs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dillilabs-com-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/dillilabs-com/hosts/dillilabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dillilabs-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dillilabs-com/integrations/dillilabs-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dillilabs-com-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/dillilabs-com/packages/dillilabs-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dillilabs-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dillilabs-com/packages/dillilabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/dillilabs-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dillilabs.com/category/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dillilabs
- group: auth
  href: https://artifacts.apis.io/dillilabs-com/security/dillilabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dillilabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dillilabs.com/
- group: start
  title: ''
  type: Portal
  url: https://deva.dillilabs.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dillilabs.com/products/email-validation-api/
- group: start
  title: ''
  type: SignUp
  url: https://deva.dillilabs.com/register
- group: company
  title: ''
  type: Blog
  url: https://www.dillilabs.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.dillilabs.com/category/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.dillilabs.com/team/
- group: company
  title: ''
  type: About
  url: https://www.dillilabs.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.dillilabs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dillilabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dillilabs.com/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/DilliLabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dillilabs/
created: '2026-11-05'
description: 'Dilli Labs LLC is a San Francisco Bay Area (Silicon Valley) software and technology consulting company founded in 2017 by an MIT alumnus. It builds web applications, iOS/Android mobile apps and Amazon Alexa/Google voice skills, offers web hosting and domain registration, and runs SaaS APIs: the Dilli Email Validation API (DEVA), IP Address Validation (DIVA), Profanity Detection (DeVIL), IP Geolocation (DIL) and a broken link checker. DEVA is also published as a remote MCP server (com.dillilabs.deva/dilli-email-validation-api-server at https://deva.dillilabs.com/mcp) in the official MCP registry. The name DILLI stands for ''Do It w/ Love and Love It''.'
image: https://www.dillilabs.com/wp-content/uploads/2019/01/dillilabs_promo_logo-1.png
json_schemas:
- name: AnalyzeRequest
  property_count: 2
  slug: dillilabs-com-analyze-request
- name: AnalyzeResponse
  property_count: 4
  slug: dillilabs-com-analyze-response
- name: UserResponse
  property_count: 2
  slug: dillilabs-com-user-response
jsonld:
- class_count: 5
  name: Dillilabs Com Context
  property_count: 11
  slug: dillilabs-com-context
layout: provider
mcp_servers:
- description: ''
  name: Dilli Labs MCP Server
  slug: mcp
modified: '2026-11-05'
name: Dilli Labs
nav: Providers
network: true
overview: 'Dilli Labs publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyze API, Health API, Privacy API, and 6 more. Tagged areas include Company, Email Verification, IP Geolocation, IP Validation, and Profanity Detection.


  The Dilli Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dilli Labs'' developer surface includes authentication, developer portal, pricing, signup flow, engineering blog, and 28 more developer resources.'
plans:
- name: Dillilabs Com Plans Pricing
  plan_count: 1
  slug: dillilabs-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dillilabs Com Rate Limits
  slug: dillilabs-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Dilli Labs API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: dillilabs-com-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 53.6
    developer_ergonomics: 42.3
    discoverability: 68.3
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dillilabs Com Authentication
  slug: dillilabs-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dillilabs Com Domain Security
  slug: dillilabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: reframe-text
  slug: dillilabs-com-reframe-text
slug: dillilabs-com
tags:
- Company
- Email Verification
- IP Geolocation
- IP Validation
- Profanity Detection
- MCP
- Software-as-a-Service
- Web Hosting
- Software Development
website: https://www.dillilabs.com/
---
