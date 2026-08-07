---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: 'The Business AI Cloud platform API. The publicly documented surface is the customer-deployed BAIC distribution: a machine-to-machine token exchange at POST /auth/m2m-token, a retrieval-augmented quest'
  name: Uniphore Business AI Cloud (BAIC) Platform API
  slug: uniphore-business-ai-cloud-baic-platform-api
- description: Uniphore's dedicated Auth0 identity tenant, which fronts sign-in for the Uniphore customer portal and issues the OAuth 2.0 / OIDC tokens used against Uniphore services. It publishes anonymous OIDC dis
  name: Uniphore Identity (OpenID Connect)
  slug: uniphore-identity-openid-connect
artifact_total: 6
common:
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
  raised a $260M Series F from NVIDIA, AMD, Snowflake and Databricks, and has acquired Orby AI, Autonom8, ActionIQ, Infosum and Jacada.'
image: https://www.uniphore.com/wp-content/uploads/2025/12/cropped-Uniphore–Bug–Gradient–Light-192x192.webp
layout: provider
modified: '2026-08-02'
name: Uniphore
nav: Providers
network: true
overview: 'Uniphore publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Conversational AI, and Customer Data Platform.


  Uniphore''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, changelog, and 23 more developer resources.'
random_paper: 83
scopes:
- name: Uniphore Scopes
  scope_count: 14
  slug: uniphore-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 34.4
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Uniphore Authentication
  slug: uniphore-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
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
- Machine Learning
- Large Language Models
- Enterprise Software
- Automation
- Customer Experience
- Knowledge Management
website: https://www.uniphore.com/
---
