---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Benefitfocus offers APIs for benefits administration (private, not publicly documented).
  name: Benefitfocus API
  slug: benefitfocus-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/benefitfocus/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.benefitfocus.com/security
- group: agent
  href: https://artifacts.apis.io/benefitfocus/llms/benefitfocus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benefitfocus-llms.txt
- group: agent
  href: https://artifacts.apis.io/benefitfocus/mcp/benefitfocus-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/benefitfocus-mcp.yml
- group: agent
  href: https://artifacts.apis.io/benefitfocus/well-known/benefitfocus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/benefitfocus-well-known.yml
- group: other
  href: https://artifacts.apis.io/benefitfocus/hosts/benefitfocus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benefitfocus-hosts.yml
- group: other
  href: https://artifacts.apis.io/benefitfocus/vendors/benefitfocus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benefitfocus-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.benefitfocus.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.benefitfocus.com/resources/news/benefitfocus-named-finalist-2024-stevie-awards-sales-customer-service
- group: start
  title: ''
  type: Login
  url: https://www.benefitfocus.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.benefitfocus.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.benefitfocus.com/resources/blog/what-is-aca-reporting
- group: docs
  title: ''
  type: Documentation
  url: https://dev.benefitfocus.com/
- group: auth
  href: https://artifacts.apis.io/benefitfocus/security/benefitfocus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/benefitfocus-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/benefitfocus/security/benefitfocus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benefitfocus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.benefitfocus.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.benefitfocus.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.benefitfocus.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.benefitfocus.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benefitfocus
coverage:
  checked: '2026-11-02'
  detail: Developer portal returns HTML but no machine-readable API specification.
  evidence:
  - status: 200
    url: https://dev.benefitfocus.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Benefitfocus provides cloud-based benefits administration software for employers and health plans, enabling data-driven management of health, dental, vision, and other employee benefits. Their platform simplifies enrollment, compliance, and reporting, helping organizations save time and money while improving employee outcomes.
image: https://www.benefitfocus.com/themes/custom/bfv1/assets/images/logo_benefitfocus.svg
layout: provider
mcp_servers:
- description: Remote MCP server at oneplace.benefitfocus.com.
  name: Benefitfocus MCP Server
  slug: benefitfocus-mcp-yml
modified: '2026-11-02'
name: Benefitfocus
nav: Providers
network: true
overview: 'Benefitfocus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Benefits, Human Resources, Software-as-a-Service, and Healthcare.


  Benefitfocus'' developer surface includes engineering blog, documentation, support, and 17 more developer resources.'
random_paper: 5
scopes:
- name: Benefitfocus Scopes
  scope_count: 0
  slug: benefitfocus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 58.3
    operational_transparency: 7.9
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Benefitfocus Authentication
  slug: benefitfocus-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Benefitfocus Domain Security
  slug: benefitfocus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Benefitfocus Trust Center
  slug: benefitfocus-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: benefitfocus
tags:
- Company
- Benefits
- Human Resources
- Software-as-a-Service
- Healthcare
- Cloud
website: https://www.benefitfocus.com
---
