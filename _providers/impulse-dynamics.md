---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 214
  human_in_the_loop: 0
  name: Impulse Dynamics Agentic Access
  operation_count: 379
  slug: impulse-dynamics-agentic-access
  summary_line: 379 operations · 214 acting
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Impulse Dynamics website at impulse-dynamics.com: the route index of the site''s content management system, catalogued as one site surface rather than as '
  name: Impulse Dynamics Website (WordPress REST)
  slug: impulse-dynamics-com-website-wordpress-rest
- baseURL: https://impulse-dynamics.com/wp-json/
  baseurl_source: declared
  description: Two Model Context Protocol servers exposed by the WordPress MCP Adapter plugin on the corporate host. Both reject anonymous JSON-RPC with HTTP 401, and the host publishes no RFC 8414 or RFC 9728 metad
  name: Impulse Dynamics MCP API
  slug: impulse-dynamics-mcp-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://impulse-dynamics.com/
- group: company
  title: ''
  type: About
  url: https://impulse-dynamics.com/company/
- group: company
  title: ''
  type: Blog
  url: https://news.impulse-dynamics.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://impulse-dynamics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://impulse-dynamics.com/company/careers/
- group: other
  title: ''
  type: Governance
  url: https://impulse-dynamics.com/company/governance/
- group: operate
  title: ''
  type: Contact
  url: https://impulse-dynamics.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impulse-dynamics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impulse-dynamics.com/privacy-policy/
- group: other
  title: ''
  type: DataProtection
  url: https://impulse-dynamics.com/data-protection-statement/
- group: auth
  title: ''
  type: Security
  url: https://impulse-dynamics.com/vulnerability-disclosure-program/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/impulse-dynamics-stock
- group: other
  href: https://artifacts.apis.io/impulse-dynamics/overlays/impulse-dynamics-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/impulse-dynamics-wp-rest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/impulse-dynamics/mcp/impulse-dynamics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/impulse-dynamics-mcp.yml
- group: build
  href: https://artifacts.apis.io/impulse-dynamics/mcp/impulse-dynamics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/impulse-dynamics-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/impulse-dynamics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/impulse-dynamics/llms/impulse-dynamics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/impulse-dynamics-llms.txt
- group: auth
  href: https://artifacts.apis.io/impulse-dynamics/authentication/impulse-dynamics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/impulse-dynamics-authentication.yml
- group: design
  href: https://artifacts.apis.io/impulse-dynamics/conventions/impulse-dynamics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/impulse-dynamics-conventions.yml
- group: design
  href: https://artifacts.apis.io/impulse-dynamics/errors/impulse-dynamics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/impulse-dynamics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/impulse-dynamics/data-model/impulse-dynamics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/impulse-dynamics-data-model.yml
- group: design
  href: https://artifacts.apis.io/impulse-dynamics/lifecycle/impulse-dynamics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/impulse-dynamics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/impulse-dynamics/conformance/impulse-dynamics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/impulse-dynamics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/impulse-dynamics/agentic-access/impulse-dynamics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/impulse-dynamics-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/impulse-dynamics/plans/impulse-dynamics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/impulse-dynamics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/impulse-dynamics/rate-limits/impulse-dynamics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/impulse-dynamics-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/impulse-dynamics/security/impulse-dynamics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/impulse-dynamics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/impulse-dynamics/security/impulse-dynamics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/impulse-dynamics-domain-security.yml
created: '2026-08-23'
description: 'Impulse Dynamics is a medical-device company that created Cardiac Contractility Modulation (CCM) therapy, delivered by the implantable Optimizer Smart and Optimizer Smart Mini pulse generators for patients with moderate-to-severe chronic heart failure who remain symptomatic despite guideline-directed medical therapy. Incorporated in 1997, with US headquarters in Marlton, New Jersey, the company won the first-ever FDA Breakthrough Device designation and received FDA approval for the Optimizer Smart in March 2019; the device has been CE marked since October 2016 and is now approved in more than 30 countries plus China. Impulse Dynamics operates no developer programme: there is no developer portal, API documentation, API reference, SDK, CLI, sandbox, pricing or sign-up, and nothing clinical or device-related is exposed as an API. It is catalogued here because its corporate website runs a live, anonymous, self-describing WordPress REST API advertising 420 routes across 30 namespaces,
  because that same install exposes two Model Context Protocol servers, and because the company publishes a substantive vulnerability disclosure programme with two PGP-published security contacts covering its medical devices, health software and infrastructure.'
image: https://impulse-dynamics.com/wp-content/uploads/2023/05/Impulse-Dynamics_Logo_1.0.png
layout: provider
mcp_servers:
- description: Two Model Context Protocol servers are live on the Impulse Dynamics corporate host. They are NOT a product MCP server for CCM therapy, the Optimizer device or any clinical data — they are the WordPres
  name: Impulse Dynamics MCP Server
  slug: impulse-dynamics-mcp-yml
modified: '2026-08-23'
name: Impulse Dynamics
nav: Providers
network: true
overview: 'Impulse Dynamics is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including MCP API, and 1 more. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  The Impulse Dynamics catalog on APIs.io includes 1 Spectral governance ruleset.


  Impulse Dynamics'' developer surface includes engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Impulse Dynamics Plans Pricing
  plan_count: 0
  slug: impulse-dynamics-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Impulse Dynamics Rate Limits
  slug: impulse-dynamics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Impulse Dynamics API Rules
  rule_count: 60
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 6
  slug: impulse-dynamics-rules
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 17.0
    developer_ergonomics: 20.8
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/impulse-dynamics/impulse-dynamics-2026-09-02T145845.png
security:
- kind: authentication
  name: Impulse Dynamics Authentication
  slug: impulse-dynamics-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Impulse Dynamics Domain Security
  slug: impulse-dynamics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Impulse Dynamics Vulnerability Disclosure
  slug: impulse-dynamics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: Find CCM therapy clinics from the Impulse Dynamics provider directory
  slug: impulse-dynamics-find-ccm-clinics
- name: Read the Impulse Dynamics newsroom and press coverage
  slug: impulse-dynamics-read-newsroom
slug: impulse-dynamics
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Implantable Devices
- Health Tech
- Life Sciences
- Clinical Trials
- MCP
- WordPress
website: https://impulse-dynamics.com/
---
