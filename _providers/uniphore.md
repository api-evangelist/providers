---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'The Business AI Cloud platform API. The publicly documented surface is the customer-deployed BAIC distribution: a machine-to-machine token exchange at POST /auth/m2m-token, a retrieval-augmented quest'
  name: Uniphore Business AI Cloud (BAIC) Platform API
  slug: uniphore-business-ai-cloud-baic-platform-api
- description: Uniphore's dedicated Auth0 identity tenant, which fronts sign-in for the Uniphore customer portal and issues the OAuth 2.0 / OIDC tokens used against Uniphore services. It publishes anonymous OIDC dis
  name: Uniphore Identity (OpenID Connect)
  slug: uniphore-identity-openid-connect
- description: The U-Capture compliance conversation-recording platform (Red Box heritage) publishes an anonymous, unauthenticated API reference on Uniphore's own documentation portal at support-rb.uniphore.com — fi
  name: Uniphore U-Capture REST APIs
  slug: uniphore-u-capture-rest-apis
artifact_total: 10
asyncapis:
- description: ''
  name: Uniphore Ucapture Webhooks
  slug: uniphore-ucapture-webhooks
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/uniphore/baic-docs/issues
- group: company
  title: ''
  type: Website
  url: https://www.uniphore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uniphore.github.io/baic-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://uniphore.github.io/baic-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://uniphore.github.io/baic-docs/#prerequisites
- group: operate
  title: ''
  type: Support
  url: https://www.uniphore.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.uniphore.com/en-US/uniphore-support
- group: company
  title: ''
  type: Blog
  url: https://www.uniphore.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uniphore
- group: start
  title: ''
  type: SignUp
  url: https://help.uniphore.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uniphore.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniphore.com/legal/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.uniphore.com/legal/aup/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.uniphore.com/legal/dpa/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.uniphore.com/legal/sla/
- group: auth
  title: ''
  type: TrustCenter
  url: security/uniphore-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.uniphore.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/uniphore-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uniphore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uniphore-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uniphore-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uniphore-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/uniphore-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uniphore-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uniphore-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.uniphore.com/legal/sla/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uniphore-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uniphore-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uniphore-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://support-rb.uniphore.com/conversa/DevelopConversa/DevelopUCaptureV2.0/DevelopUCapture/DevelopUCapture.htm
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uniphore-ucapture-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uniphore-ucapture-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uniphore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uniphore-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/uniphore-components.yml
- group: company
  title: ''
  type: Partners
  url: https://www.uniphore.com/partners/
- group: operate
  title: ''
  type: Contact
  url: https://www.uniphore.com/contact/
created: '2026-08-02'
description: 'Uniphore is an enterprise AI company — "The Business AI Company" — founded in 2008 and headquartered in Palo Alto, California. Its flagship platform, the Business AI Cloud (BAIC), is a sovereign, composable and secure AI platform organised into four layers: a Data Layer for zero-copy access to enterprise data, a Knowledge Layer for retrieval and grounding, a Model Layer for serving and fine-tuning small and large language models without vendor lock-in, and an Agentic Layer for no-code, BPMN-based agent orchestration. Products span Marketing AI (CDP Agent), Sales AI, People AI and Customer Service AI (real-time guidance, self-service, conversation insights and communication recording agents). The platform ships as a managed multi-region cloud service and as a customer-deployed Kubernetes/Helm distribution of 13 microservices with a documented machine-to-machine token exchange, a /v1 question-answering API and an OpenAI-compatible LLM inference proxy. Uniphore serves 2,000+ enterprises,
  raised a $260M Series F from NVIDIA, AMD, Snowflake and Databricks, and has acquired Orby AI, Autonom8, ActionIQ, Infosum and Jacada. Its one anonymous API reference sits apart from uniphore.com, on the U-Capture documentation portal at support-rb.uniphore.com, which documents fifteen REST API families plus a webhook/SNMP health-alert surface without publishing a machine-readable contract.'
image: https://www.uniphore.com/wp-content/uploads/2025/12/cropped-Uniphore–Bug–Gradient–Light-192x192.webp
layout: provider
modified: '2026-08-14'
name: Uniphore
nav: Providers
network: true
overview: 'Uniphore publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Conversational AI, and Customer Data Platform.


  The Uniphore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uniphore''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, changelog, and 30 more developer resources.'
plans:
- name: Uniphore Plans Pricing
  plan_count: 0
  slug: uniphore-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Uniphore Rate Limits
  slug: uniphore-rate-limits
scopes:
- name: Uniphore Scopes
  scope_count: 14
  slug: uniphore-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 0.0
  previous_composite: 41.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uniphore/refs/heads/main/screenshots/uniphore-2026-08-17T082608.png
security:
- kind: authentication
  name: Uniphore Authentication
  slug: uniphore-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Uniphore Domain Security
  slug: uniphore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Uniphore Trust Center
  slug: uniphore-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, PCI DSS v4.0.1, HIPAA, GDPR, FIPS 140-2, FIPS 140-3, CASA Tier 2, NIST CSF, EU AI Act
slug: uniphore
tags:
- Company
- Artificial Intelligence
- Agents
- Conversational AI
- Customer Data Platform
- Contact Center
- Machine-Learning
- Large Language Models
- Enterprise Software
- Automation
- Customer Experience
- Knowledge-Management
website: https://www.uniphore.com/
---
