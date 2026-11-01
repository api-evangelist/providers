---
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 77
  human_in_the_loop: 1
  name: Allocations Agentic Access
  operation_count: 167
  slug: allocations-agentic-access
  summary_line: 167 operations · 77 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Allocations API provides access to fund administration operations.
  name: Allocations API
  slug: allocations-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Accreditations API from Allocations — 3 operation(s) for accreditations.
  name: Allocations Accreditations API
  slug: allocations-accreditations-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Announcements API from Allocations — 2 operation(s) for announcements.
  name: Allocations Announcements API
  slug: allocations-announcements-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Assets API from Allocations — 2 operation(s) for assets.
  name: Allocations Assets API
  slug: allocations-assets-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Currency storage and movement
  name: Allocations Banking API
  slug: allocations-banking-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Closes API from Allocations — 3 operation(s) for closes.
  name: Allocations Closes API
  slug: allocations-closes-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: SPVs and Funds
  name: Allocations Deals API
  slug: allocations-deals-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Distributions API from Allocations — 3 operation(s) for distributions.
  name: Allocations Distributions API
  slug: allocations-distributions-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The DistributionsInvestments API from Allocations — 2 operation(s) for distributionsinvestments.
  name: Allocations Distributions Investments API
  slug: allocations-distributionsinvestments-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Document Generation and Storage
  name: Allocations Documents API
  slug: allocations-documents-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Legal Structures for SPVs and Funds
  name: Allocations Entities API
  slug: allocations-entities-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: File Storage and Retrieval
  name: Allocations Files API
  slug: allocations-files-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Representations of Individuals and Corporations
  name: Allocations Identities API
  slug: allocations-identities-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Investment details
  name: Allocations Investments API
  slug: allocations-investments-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Ledger API from Allocations — 11 operation(s) for ledger.
  name: Allocations Ledger API
  slug: allocations-ledger-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Call-to-actions and informational data
  name: Allocations Notifications API
  slug: allocations-notifications-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Client Information and Account Grouping
  name: Allocations Organizations API
  slug: allocations-organizations-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Providers API from Allocations — 3 operation(s) for providers.
  name: Allocations Providers API
  slug: allocations-providers-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Standard Data References to be used with other objects
  name: Allocations Static References API
  slug: allocations-static-references-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Engage the Allocations support team
  name: Allocations Support Tickets API
  slug: allocations-support-tickets-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: Deal and Entity related taxes
  name: Allocations Taxes API
  slug: allocations-taxes-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The Transfer Requests API from Allocations — 5 operation(s) for transfer requests.
  name: Allocations Transfer Requests API
  slug: allocations-transfer-requests-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The TransferInformation API from Allocations — 3 operation(s) for transferinformation.
  name: Allocations Transfer Information API
  slug: allocations-transferinformation-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The XeroAuthController API from Allocations — 5 operation(s) for xeroauthcontroller.
  name: Allocations Xero Auth Controller API
  slug: allocations-xeroauthcontroller-api
- baseURL: https://api.allocations.com
  baseurl_source: declared
  description: The XeroInvoicesController API from Allocations — 7 operation(s) for xeroinvoicescontroller.
  name: Allocations Xero Invoices Controller API
  slug: allocations-xeroinvoicescontroller-api
artifact_total: 37
common:
- group: other
  href: https://artifacts.apis.io/allocations/capabilities/allocations-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/allocations-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/allocations/agentic-access/allocations-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/allocations-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/allocations/plans/allocations-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allocations-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allocations/rules/allocations-rules.yml
  title: ''
  type: Spectral
  url: rules/allocations-rules.yml
- group: design
  href: https://artifacts.apis.io/allocations/json-ld/allocations-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allocations-context.jsonld
- group: design
  href: https://artifacts.apis.io/allocations/vocabulary/allocations-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allocations-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/allocations/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/allocations/data-model/allocations-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allocations-data-model.yml
- group: design
  href: https://artifacts.apis.io/allocations/errors/allocations-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allocations-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allocations/conformance/allocations-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allocations-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allocations/llms/allocations-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allocations-llms.txt
- group: agent
  href: https://artifacts.apis.io/allocations/well-known/allocations-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allocations-well-known.yml
- group: other
  href: https://artifacts.apis.io/allocations/hosts/allocations-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allocations-hosts.yml
- group: other
  href: https://artifacts.apis.io/allocations/vendors/allocations-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allocations-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.allocations.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.allocations.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.allocations.com/insights/registered-agent-duties-for-a-deal-spv
- group: company
  title: ''
  type: Newsroom
  url: https://www.allocations.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.allocations.com/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.allocations.com/investor-onboarding/how-to-signup
- group: auth
  href: https://artifacts.apis.io/allocations/authentication/allocations-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allocations-authentication.yml
- group: auth
  href: https://artifacts.apis.io/allocations/security/allocations-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allocations-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allocations.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.allocations.com
- group: company
  title: ''
  type: Blog
  url: https://www.allocations.com/insights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.allocations.com/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allocations.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allocations.com/privacy-policy
created: '2026-09-24'
description: Allocations provides a cloud‑based fund administration platform that enables general partners, syndicates and emerging managers to launch and manage SPVs and private funds. The service automates legal formation, banking, compliance, investor onboarding and reporting, offering pricing plans from $9,950 for single‑SPV setups to enterprise solutions. Backed by venture capital, Allocations serves over 30,000 clients and has transacted more than $5 billion in assets across 1,800+ private funds.
finops:
- has_sources: true
  method: derived
  name: Allocations Finops
  primary_unit: ''
  service_category: ''
  slug: allocations-finops
  template: true
image: https://framerusercontent.com/assets/Ck8iMxhd72aQ8s11wWAttjthVs.png
jsonld:
- class_count: 120
  name: Allocations Context
  property_count: 482
  slug: allocations-context
layout: provider
modified: '2026-09-24'
name: Allocations
nav: Providers
network: true
overview: 'Allocations publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accreditations API, Announcements API, Assets API, and 22 more. Tagged areas include Fintech, Fund Administration, Private Markets, Software-as-a-Service, and Investment Platform.


  The Allocations catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Allocations'' developer surface includes signup flow, getting-started guide, authentication, documentation, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Allocations Plans Pricing
  plan_count: 6
  slug: allocations-plans-pricing
- name: Allocations Price Estimates
  plan_count: 0
  slug: allocations-price-estimates
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Allocations API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 4
  slug: allocations-rules
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 55.1
    developer_ergonomics: 37.5
    discoverability: 69.6
    operational_transparency: 15.8
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Allocations Authentication
  slug: allocations-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Allocations Domain Security
  slug: allocations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: allocations-bank-account-setup
  slug: allocations-bank-account-setup
- name: allocations-create-and-list-ledger-entries
  slug: allocations-create-and-list-ledger-entries
- name: allocations-manage-entity
  slug: allocations-manage-entity
- name: allocations-notifications-read
  slug: allocations-notifications-read
slug: allocations
tags:
- Fintech
- Fund Administration
- Private Markets
- Software-as-a-Service
- Investment Platform
website: https://www.allocations.com
---
