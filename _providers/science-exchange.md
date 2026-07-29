---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 23
apis:
- description: Addresses resource.
  name: Science Exchange addresses API
  slug: science-exchange-addresses-api
- description: Attachments resource.
  name: Science Exchange attachments API
  slug: science-exchange-attachments-api
- description: CurrencyCodes resource.
  name: Science Exchange currency_codes API
  slug: science-exchange-currency-codes-api
- description: ExperimentTypeFields resource.
  name: Science Exchange experiment_type_fields API
  slug: science-exchange-experiment-type-fields-api
- description: ExperimentTypes resource.
  name: Science Exchange experiment_types API
  slug: science-exchange-experiment-types-api
- description: Facilities resource.
  name: Science Exchange facilities API
  slug: science-exchange-facilities-api
- description: FacilityMembers resource.
  name: Science Exchange facility_members API
  slug: science-exchange-facility-members-api
- description: FacilityPhotos resource.
  name: Science Exchange facility_photos API
  slug: science-exchange-facility-photos-api
- description: Groups resource.
  name: Science Exchange groups API
  slug: science-exchange-groups-api
- description: LineItems resource.
  name: Science Exchange line_items API
  slug: science-exchange-line-items-api
- description: PricingUnits resource.
  name: Science Exchange pricing_units API
  slug: science-exchange-pricing-units-api
- description: QuoteVersions resource.
  name: Science Exchange quote_versions API
  slug: science-exchange-quote-versions-api
- description: Quotes resource.
  name: Science Exchange quotes API
  slug: science-exchange-quotes-api
- description: Ratings resource.
  name: Science Exchange ratings API
  slug: science-exchange-ratings-api
- description: RFQCollaborators resource.
  name: Science Exchange rfq_collaborators API
  slug: science-exchange-rfq-collaborators-api
- description: RFQEvents resource.
  name: Science Exchange rfq_events API
  slug: science-exchange-rfq-events-api
- description: RFQFields resource.
  name: Science Exchange rfq_fields API
  slug: science-exchange-rfq-fields-api
- description: RFQMessages resource.
  name: Science Exchange rfq_messages API
  slug: science-exchange-rfq-messages-api
- description: RFQs resource.
  name: Science Exchange rfqs API
  slug: science-exchange-rfqs-api
- description: Services resource.
  name: Science Exchange services API
  slug: science-exchange-services-api
- description: TagContexts resource.
  name: Science Exchange tag_contexts API
  slug: science-exchange-tag-contexts-api
- description: Tags resource.
  name: Science Exchange tags API
  slug: science-exchange-tags-api
- description: Users resource.
  name: Science Exchange users API
  slug: science-exchange-users-api
artifact_total: 27
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/science-exchange-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.scienceexchange.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://demo.scienceexchange.com/api-docs/providers
- group: docs
  title: ''
  type: Documentation
  url: https://demo.scienceexchange.com/api-docs/providers
- group: docs
  title: ''
  type: APIReference
  url: https://demo.scienceexchange.com/api-docs/providers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scienceexchange
- group: company
  title: ''
  type: Blog
  url: https://www.scienceexchange.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.scienceexchange.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scienceexchange.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scienceexchange.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.scienceexchange.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.scienceexchange.com/platform/security
- group: auth
  title: ''
  type: Trust
  url: https://www.scienceexchange.com/trust
- group: build
  title: ''
  type: Packages
  url: packages/science-exchange-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/science-exchange-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/science-exchange-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/science-exchange-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/science-exchange-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/science-exchange-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/science-exchange-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/science-exchange-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/science-exchange-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/science-exchange-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/science-exchange-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/science-exchange-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Science Exchange is an R&D supplier orchestration and procurement platform for life-sciences organizations. It runs a marketplace of 3,800+ pre-qualified scientific service providers under a single master service agreement, and streamlines supplier sourcing, onboarding, contracting, compliance, and payment. The platform integrates with ERP (SAP, Oracle, Workday), P2P (Ariba, Coupa), and SSO/SAML identity systems, and exposes a read-only Providers REST API (v1) that lets scientific-service suppliers pull their RFQs, quotes, services, facilities, line items, ratings, tags, and users. Founded in 2011 and headquartered in Palo Alto, California; backed by a16z, Index Ventures, and Union Square Ventures.
image: https://avatars.githubusercontent.com/scienceexchange
layout: provider
mcp_servers:
- description: ''
  name: science-exchange-mcp.yml
  slug: science-exchange-mcpyml
modified: '2026-07-21'
name: Science Exchange
nav: Providers
network: true
overview: 'Science Exchange publishes 23 APIs on the [APIs.io](https://apis.io/) network, including addresses API, attachments API, currency_codes API, and 20 more. Tagged areas include Company, Life Sciences, Research and Development, Scientific Services, and Procurement.


  Science Exchange''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 46.5
  delta: -3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 49.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Science Exchange Authentication
  slug: science-exchange-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Science Exchange Domain Security
  slug: science-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Science Exchange Trust Center
  slug: science-exchange-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: science-exchange
tags:
- Company
- Life Sciences
- Research and Development
- Scientific Services
- Procurement
- Marketplace
- Supplier Management
- Biotech
- Pharmaceuticals
- API
website: https://www.scienceexchange.com
---
