---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Claroty Agentic Access
  operation_count: 9
  slug: claroty-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: Remote MCP server on the Claroty customer community, OAuth-gated (scopes mcp:read, mcp:write) and unavailable to guest users.
  name: Claroty Community MCP
  slug: community-mcp
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Authenticate API from Claroty — 1 operation(s) for authenticate.
  name: Claroty Authenticate API
  slug: claroty-authenticate-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Health API from Claroty — 1 operation(s) for health.
  name: Claroty Health API
  slug: claroty-health-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Is Key Registered API from Claroty — 1 operation(s) for is key registered.
  name: Claroty Is Key Registered API
  slug: claroty-is-key-registered-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Jwks API from Claroty — 1 operation(s) for jwks.
  name: Claroty Jwks API
  slug: claroty-jwks-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The JWThenticator API from Claroty — 1 operation(s) for jwthenticator.
  name: Claroty JW Thenticator API
  slug: claroty-jwthenticator-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Refresh API from Claroty — 1 operation(s) for refresh.
  name: Claroty Refresh API
  slug: claroty-refresh-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Register Key API from Claroty — 1 operation(s) for register key.
  name: Claroty Register Key API
  slug: claroty-register-key-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Validate API from Claroty — 1 operation(s) for validate.
  name: Claroty Validate API
  slug: claroty-validate-api
- baseURL: https://{jwthenticator-host}
  baseurl_source: declared
  description: The Validate Request API from Claroty — 1 operation(s) for validate request.
  name: Claroty Validate Request API
  slug: claroty-validate-request-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/claroty/agentic-access/claroty-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/claroty-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/claroty/rules/claroty-rules.yml
  title: ''
  type: Spectral
  url: rules/claroty-rules.yml
- group: design
  href: https://artifacts.apis.io/claroty/json-ld/claroty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claroty-context.jsonld
- group: design
  href: https://artifacts.apis.io/claroty/vocabulary/claroty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claroty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claroty/data-model/claroty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claroty-data-model.yml
- group: design
  href: https://artifacts.apis.io/claroty/errors/claroty-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/claroty-problem-types.yml
- group: design
  href: https://artifacts.apis.io/claroty/conformance/claroty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claroty-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claroty/llms/claroty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claroty-llms.txt
- group: agent
  href: https://artifacts.apis.io/claroty/well-known/claroty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claroty-well-known.yml
- group: other
  href: https://artifacts.apis.io/claroty/hosts/claroty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claroty-hosts.yml
- group: build
  href: https://artifacts.apis.io/claroty/integrations/claroty-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/claroty-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/claroty/vendors/claroty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claroty-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.claroty.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.claroty.com/team82/disclosure-dashboard/feed/atom
- group: auth
  href: https://artifacts.apis.io/claroty/security/claroty-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/claroty-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/claroty/security/claroty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claroty-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.claroty.com/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/claroty
- group: company
  title: ''
  type: Blog
  url: https://www.claroty.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.claroty.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://portal.claroty.com/#/page/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claroty.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claroty.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.claroty.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.claroty.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.claroty.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.claroty.com/leadership
- group: start
  title: ''
  type: Login
  url: https://community.claroty.com/User/Login
created: '2026-07-17'
description: Claroty is a cybersecurity company that protects cyber-physical systems (CPS) across industrial, healthcare, commercial, and public-sector environments. Its AI-powered platform delivers asset discovery, exposure and vulnerability management, threat detection, and secure remote access for operational technology (OT), IoT, and the extended internet of things (XIoT) that traditional IT security tools cannot adequately protect. Claroty serves more than 1,300 customers across 60+ countries, including 24 of the Fortune 100, and its Team82 research group publishes original vulnerability research and open-source ICS security tooling. This profile was seeded as a venture-portfolio lead and enriched by the API Evangelist pipeline; Claroty publishes no public product API or developer portal, so enrichment is limited to company identity, GitHub open-source presence, and security/compliance posture.
image: https://web-assets.claroty.com/seo/og-default-2.png
json_schemas:
- name: AuthRequest
  property_count: 2
  slug: claroty-auth-request
- name: BoolResponse
  property_count: 2
  slug: claroty-bool-response
- name: JWKSResponse
  property_count: 6
  slug: claroty-jwksresponse
- name: RefreshRequest
  property_count: 2
  slug: claroty-refresh-request
- name: RegisterKeyRequest
  property_count: 2
  slug: claroty-register-key-request
- name: TokenResponse
  property_count: 2
  slug: claroty-token-response
jsonld:
- class_count: 8
  name: Claroty Context
  property_count: 12
  slug: claroty-context
layout: provider
mcp_servers:
- description: Remote MCP endpoint served by the Claroty customer community (community.claroty.com). Anonymous tools/list returns a JSON-RPC error requiring login; the protected-resource metadata advertises OAuth wi
  name: Claroty Community MCP Server
  slug: claroty-community-mcp-server
modified: '2026-10-06'
name: Claroty
nav: Providers
network: true
overview: 'Claroty publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authenticate API, Health API, Is Key Registered API, and 7 more. Tagged areas include Company, Cybersecurity, OT Security, Cyber-Physical Systems, and IoT Security.


  The Claroty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claroty''s developer surface includes engineering blog, support, and 26 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Claroty API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: claroty-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 53.0
    developer_ergonomics: 11.9
    discoverability: 76.7
    operational_transparency: 5.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/claroty/claroty-2026-07-25T205512.png
security:
- kind: domain-security
  name: Claroty Domain Security
  slug: claroty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Claroty Trust Center
  slug: claroty-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: claroty
tags:
- Company
- Cybersecurity
- OT Security
- Cyber-Physical Systems
- IoT Security
- Industrial Control Systems
- Threat Detection
- Exposure Management
- Healthcare Security
website: https://www.claroty.com/
---
