---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST-based interface exposing the Kinaxis Maestro (RapidResponse) supply chain planning platform for data integration, process orchestration, and insight embedding. Enables reading and writing plannin
  name: Kinaxis RapidResponse REST API
  slug: rapidresponse-rest-api
- description: A low-code and code-first development environment embedded in the Kinaxis Maestro platform that enables building custom supply chain applications, algorithms, data models, integration jobs, visualizat
  name: Kinaxis Developer Studio
  slug: developer-studio
- description: A production-ready Model Context Protocol (MCP) server that provides AI agents and LLM-powered applications with standardized OAuth 2.0-secured access to Kinaxis Maestro supply chain planning data and
  name: Kinaxis MCP Server
  slug: mcp-server
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/kinaxis/well-known/kinaxis-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kinaxis-aws-security.txt
- group: operate
  title: ''
  type: Support
  url: https://help.kinaxis.com/home.aspx
- group: auth
  title: ''
  type: Compliance
  url: https://www.kinaxis.com/en/trust-center
- group: agent
  href: https://artifacts.apis.io/kinaxis/llms/kinaxis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kinaxis-llms.txt
- group: auth
  href: https://artifacts.apis.io/kinaxis/well-known/kinaxis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kinaxis-security.txt
- group: agent
  href: https://artifacts.apis.io/kinaxis/well-known/kinaxis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kinaxis-well-known.yml
- group: other
  href: https://artifacts.apis.io/kinaxis/hosts/kinaxis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kinaxis-hosts.yml
- group: build
  href: https://artifacts.apis.io/kinaxis/integrations/kinaxis-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/kinaxis-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/kinaxis/vendors/kinaxis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kinaxis-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kinaxis.com/en/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://www.kinaxis.com/en/continuous-learning-services/register-and-subscribe-training
- group: auth
  title: ''
  type: Security
  url: https://www.kinaxis.com/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kinaxis.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.kinaxis.com/en/news
- group: other
  title: ''
  type: Leadership
  url: https://www.kinaxis.com/en/leadership
- group: auth
  href: https://artifacts.apis.io/kinaxis/security/kinaxis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kinaxis-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kinaxis/security/kinaxis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinaxis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kinaxis/security/kinaxis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinaxis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kinaxis.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.kinaxis.com/s/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Kinaxis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kinaxis
- group: company
  title: ''
  type: Blog
  url: https://www.kinaxis.com/en/blog/main
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kinaxis.com/en/contact-us
- group: other
  title: ''
  type: X
  url: https://x.com/kinaxis
- group: commercial
  href: https://artifacts.apis.io/kinaxis/plans/kinaxis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kinaxis-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/kinaxis/finops/kinaxis-finops.yml
  title: ''
  type: FinOps
  url: finops/kinaxis-finops.yml
coverage:
  checked: '2026-10-20'
  detail: The RapidResponse/Maestro REST API is documented only inside the Kinaxis Knowledge Network, a Salesforce community at knowledge.kinaxis.com that renders a 376-character login shell to anonymous readers and 401s its /mcp/v1 path; no public OpenAPI, SDK or developer reference exists.
  evidence:
  - status: 200
    url: https://knowledge.kinaxis.com/s/
  - status: 401
    url: https://knowledge.kinaxis.com/mcp/v1
  - status: 404
    url: https://knowledge.kinaxis.com/s/article/RapidResponse-REST-API
  - status: 302
    url: https://rapidresponse.kinaxis.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Kinaxis is a concurrent supply chain planning platform — branded Maestro (formerly RapidResponse) — that provides REST APIs for supply chain orchestration, scenario modeling, demand sensing, and supply planning across global manufacturing and distribution networks. The platform offers an AI-infused intelligence engine, digital twin simulation, and a Developer Studio for building custom applications and algorithms on top of the supply chain data fabric.
finops:
- has_sources: false
  method: generated
  name: Kinaxis Finops
  primary_unit: ''
  service_category: ''
  slug: kinaxis-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kinaxis.png
layout: provider
modified: '2026-06-13'
name: Kinaxis
nav: Providers
network: true
overview: 'Kinaxis is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Supply Chain Planning, Demand Sensing, Scenario Modeling, and Supply Planning.


  Kinaxis'' developer surface includes support, signup flow, documentation, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Kinaxis Plans Pricing
  plan_count: 1
  slug: kinaxis-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Kinaxis Rate Limits
  slug: kinaxis-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 80.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kinaxis/kinaxis-2026-06-20T184039.png
security:
- kind: domain-security
  name: Kinaxis Domain Security
  slug: kinaxis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kinaxis Vulnerability Disclosure
  slug: kinaxis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kinaxis Trust Center
  slug: kinaxis-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kinaxis
tags:
- Supply Chain
- Supply Chain Planning
- Demand Sensing
- Scenario Modeling
- Supply Planning
- Inventory Optimization
- S&OP
- Control Tower
- Enterprise Software
- Artificial Intelligence
- Canada
website: https://www.kinaxis.com/en
---
