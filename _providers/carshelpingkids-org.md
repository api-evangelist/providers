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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent API for submitting vehicle donation requests and retrieving intake links.
  name: Cars Helping Kids Agent API
  slug: cars-helping-kids-agent-api
- baseURL: https://carshelpingkids.org
  baseurl_source: declared
  description: Submit an explicitly authorized vehicle-donation request to Cars Helping Kids for case review. Cars Helping Kids is the vehicle-donation program operated by Fainting Goat Foundation Co Inc, EIN 99-047
  name: Cars Helping Kids — Car Donations Agent API API
  slug: cars-helping-kids-car-donations-agent-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/rules/carshelpingkids-org-rules.yml
  title: ''
  type: Spectral
  url: rules/carshelpingkids-org-rules.yml
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/json-ld/carshelpingkids-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carshelpingkids-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/vocabulary/carshelpingkids-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carshelpingkids-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/conventions/carshelpingkids-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/carshelpingkids-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/conventions/carshelpingkids-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carshelpingkids-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/conformance/carshelpingkids-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carshelpingkids-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carshelpingkids-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/data-model/carshelpingkids-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carshelpingkids-org-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://carshelpingkids.org/privacy
- group: design
  href: https://artifacts.apis.io/carshelpingkids-org/errors/carshelpingkids-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carshelpingkids-org-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/carshelpingkids-org/llms/carshelpingkids-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carshelpingkids-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/carshelpingkids-org/mcp/carshelpingkids-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carshelpingkids-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carshelpingkids-org/well-known/carshelpingkids-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carshelpingkids-org-security.txt
- group: agent
  href: https://artifacts.apis.io/carshelpingkids-org/well-known/carshelpingkids-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carshelpingkids-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/carshelpingkids-org/hosts/carshelpingkids-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carshelpingkids-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/carshelpingkids-org/vendors/carshelpingkids-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carshelpingkids-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carshelpingkids.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carshelpingkids.org/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://carshelpingkids.org/press
- group: auth
  href: https://artifacts.apis.io/carshelpingkids-org/security/carshelpingkids-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carshelpingkids-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carshelpingkids-org/security/carshelpingkids-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carshelpingkids-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carshelpingkids.org/
- group: docs
  title: ''
  type: Documentation
  url: https://carshelpingkids.org/about
created: '2026-11-03'
description: Cars Helping Kids is a 501(c)(3) nonprofit program of the Fainting Goat Foundation that provides free vehicle towing and donation services. Donors can give cars, trucks, motorcycles, boats, RVs, or trailers, and the organization handles title paperwork and pickup. Net proceeds fund school supplies, food support, tutoring, and seasonal assistance for children in Georgia.
image: https://carshelpingkids.org/og-image.jpg
json_schemas:
- name: AuthorizedDonationRequest
  property_count: 6
  slug: carshelpingkids-org-authorized-donation-request
- name: DonationReceipt
  property_count: 9
  slug: carshelpingkids-org-donation-receipt
jsonld:
- class_count: 6
  name: Carshelpingkids Org Context
  property_count: 33
  slug: carshelpingkids-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at carshelpingkids.org.
  name: Cars Helping Kids MCP Server
  slug: carshelpingkids-org-mcp-yml
modified: '2026-11-03'
name: Cars Helping Kids
nav: Providers
network: true
overview: 'Cars Helping Kids publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including — Car Donations Agent API API, and 1 more. Tagged areas include Charity, Non-Profit, Vehicle Donation, Education Support, and Georgia.


  The Cars Helping Kids catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cars Helping Kids'' developer surface includes documentation and 22 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Cars Helping Kids API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: carshelpingkids-org-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 11.2
    discoverability: 65.8
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carshelpingkids Org Domain Security
  slug: carshelpingkids-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carshelpingkids Org Vulnerability Disclosure
  slug: carshelpingkids-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carshelpingkids-org
tags:
- Charity
- Non-Profit
- Vehicle Donation
- Education Support
- Georgia
website: https://carshelpingkids.org/
---
