---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The public UI APIs available in the o9 platform, used to access the GraphCube server data and its model in order to query and visualize planning data. The API reference is published in the o9 Guide bu
  name: o9 Platform API
  slug: platform-api
- description: A list of all SAP and Inbound Staging APIs used by the batch process for o9 Reference Model integration. Documented in the o9 Guide behind the same OAuth gate as the Platform API.
  name: o9 Reference Model API
  slug: ref-model-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/o9-solutions-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/o9-solutions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/o9-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://o9solutions.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://guide.o9solutions.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documents.o9solutions.com/
- group: docs
  title: ''
  type: APIReference
  url: https://guide.o9solutions.com/Resources/ApiDocs
- group: operate
  title: ''
  type: Support
  url: https://support.o9solutions.com/
- group: operate
  title: ''
  type: Community
  url: https://community.o9solutions.com/
- group: company
  title: ''
  type: Blog
  url: https://o9solutions.com/resources?type=post
- group: start
  title: ''
  type: SignUp
  url: https://guide.o9solutions.com/Home/LogIn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://o9solutions.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://o9solutions.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://o9solutions.com/security/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: Compliance
  url: https://o9solutions.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/o9-solutions-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/o9-solutions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/o9-solutions-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/o9-solutions-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/o9-solutions-lifecycle.yml
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/o9-solutions_stock/
created: '2026-07-31'
description: o9 Solutions is an enterprise AI platform for integrated planning and decision-making, founded in 2009 by Sanjiv Sidhu (previously founder of i2 Technologies) and Chakri Gottemukkala, and headquartered in Dallas, Texas. Its o9 Digital Brain platform unifies supply chain, commercial and financial planning on a patented Enterprise Knowledge Graph (EKG) — an always-on digital twin of the enterprise — supporting demand planning, AI/ML forecasting, supply chain master planning, control tower, multi-echelon inventory optimization, supplier relationship management, revenue growth management, merchandise planning and ESG planning. The platform ingests enterprise data via SFTP batch, REST API, SOAP XML and streaming, with connectors to SAP, Oracle, Snowflake, Databricks and Google BigQuery. o9 publishes two API surfaces — the o9 Platform API (public UI APIs over the GraphCube server) and the o9 Reference Model API (SAP and inbound staging batch integration) — but both API references
  sit behind the customer/partner OAuth login at guide.o9solutions.com, so no machine-readable contract is publicly available.
image: https://cms.o9solutions.com/wp-content/uploads/2025/05/cropped-favicon-o9-2.webp
layout: provider
modified: '2026-07-31'
name: o9 Solutions
nav: Providers
network: true
overview: 'o9 Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Supply Chain Planning, Integrated Business Planning, and Demand Planning.


  o9 Solutions'' developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 3
scopes:
- name: O9 Solutions Scopes
  scope_count: 3
  slug: o9-solutions-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 28.8
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/o9-solutions/refs/heads/main/screenshots/o9-solutions-2026-08-07T185839.png
security:
- kind: authentication
  name: O9 Solutions Authentication
  slug: o9-solutions-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: O9 Solutions Domain Security
  slug: o9-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: O9 Solutions Vulnerability Disclosure
  slug: o9-solutions-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: O9 Solutions Trust Center
  slug: o9-solutions-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, SOC 1, SOC 2, BSI C5, TISAX, NIST CSF 1.1
slug: o9-solutions
tags:
- Company
- Supply Chain
- Supply Chain Planning
- Integrated Business Planning
- Demand Planning
- Enterprise Software
- Artificial Intelligence
- Knowledge Graph
- Decision Intelligence
- Retail Planning
- Revenue Growth Management
- Enterprise Resource Planning
website: https://o9solutions.com
---
