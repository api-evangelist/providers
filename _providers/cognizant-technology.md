---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: '{scheme}://{host}:{port}/api/v1'
  baseurl_source: declared
  description: 'The HTTP/gRPC/MCP service surface of Neuro SAN (Neuro AI System of Agent Networks), the open-source multi-agent orchestration framework published by Cognizant AI Lab under Apache-2.0. Four operations:'
  name: Cognizant Neuro SAN Agent Service
  slug: cognizant-neuro-san-agent-service
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognizant-technology-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognizant
- group: company
  title: ''
  type: Website
  url: https://www.cognizant.com/
- group: other
  title: ''
  type: AI Lab
  url: https://www.cognizant.com/us/en/ai-lab
- group: other
  title: ''
  type: Platforms
  url: https://www.cognizant.com/us/en/services/cognizant-platforms
- group: other
  title: ''
  type: Neuro AI Decisioning
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-generative-ai-adoption
- group: other
  title: ''
  type: Neuro AI Enterprise Core
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-enterprise-core
- group: other
  title: ''
  type: Neuro AI Engineering
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-engineering
- group: other
  title: ''
  type: Neuro AI for IT Operations
  url: https://www.cognizant.com/us/en/services/cognizant-platforms/neuro-ai-it-operations
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cognizant-ai-lab
- group: other
  title: ''
  type: Neuro SAN Studio
  url: https://github.com/cognizant-ai-lab/neuro-san-studio
- group: company
  title: ''
  type: News
  url: https://news.cognizant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognizant.com/us/en/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cognizant.com/us/en/about-cognizant/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.cognizant.com/us/en/insights/insights-blog
- group: build
  title: ''
  type: Packages
  url: packages/cognizant-technology-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cognizant-technology-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cognizant-technology-cli.yml
- group: design
  title: ''
  type: Components
  url: components/cognizant-technology-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cognizant-technology-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cognizant-technology-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cognizant-technology-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cognizant-technology-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognizant-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cognizant-technology-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cognizant-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognizant-technology-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cognizant-ai-lab/neuro-san/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cognizant-ai-lab/neuro-san/tree/main/quick-start
- group: operate
  title: ''
  type: Support
  url: https://github.com/cognizant-ai-lab/neuro-san/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cognizant-ai-lab/neuro-san/releases
created: '2025-03-21'
description: 'Cognizant Technology Solutions is a multinational information technology services and consulting company that provides digital, technology, consulting, and operations services to clients worldwide. Cognizant publishes no hosted, general-purpose commercial API and operates no developer portal - developer.cognizant.com and api.cognizant.com do not resolve. It does, however, publish a real machine-readable API contract: Cognizant AI Lab releases Neuro SAN (Neuro AI System of Agent Networks), an Apache-2.0 multi-agent orchestration framework whose agent service ships four .proto files defining two gRPC services, a generated OpenAPI 3.0.3 document the running server publishes at /api/v1/docs, and an MCP 2025-06-18 endpoint that exposes each public agent network as a callable tool. The framework is self-hosted - Cognizant ships the software and the operator runs the server - so there is no Cognizant-operated endpoint, no pricing, and no rate limit to publish. Six first-party Python
  packages are on PyPI, led by neuro-san (0.7.0, 149 releases, actively developed). The commercial Neuro AI platform family (Neuro AI Decisioning, Neuro AI Enterprise Core, Neuro AI Engineering, Neuro AI for IT Operations) and other delivered platforms are engaged through consulting rather than self-service APIs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognizant-technology.png
layout: provider
mcp_servers:
- description: ''
  name: Neuro SAN MCP service
  slug: neuro-san-mcp-service
modified: '2026-09-05'
name: Cognizant Technology Solutions
nav: Providers
network: true
overview: 'Cognizant Technology Solutions publishes 1 API on the [APIs.io](https://apis.io/) network: Cognizant Neuro SAN Agent Service. Tagged areas include AI Platform, Consulting, Digital Transformation, IT Services, and Multi-Agent.


  Cognizant Technology Solutions'' developer surface includes GitHub presence, product news, engineering blog, CLI, changelog, documentation, getting-started guide, and 25 more developer resources.'
plans:
- name: Cognizant Technology Plans Pricing
  plan_count: 0
  slug: cognizant-technology-plans-pricing
press:
- date: '2026-05-25'
  title: Cognizant and OpenAI Partner to Reshape Enterprise ...
  url: https://www.prnewswire.com/news-releases/cognizant-and-openai-partner-to-reshape-enterprise-software-engineering-with-codex-302748608.html
- date: '2026-05-25'
  title: Cognizant Press Releases, Company News
  url: https://news.cognizant.com/newsannouncements
- date: '2026-05-25'
  title: Investor Relations | Cognizant
  url: https://investors.cognizant.com/home/default.aspx
- date: '2026-05-25'
  title: Cognizant News & Events | Cognizant Press Releases ...
  url: https://news.cognizant.com/
- date: '2026-05-25'
  title: Cognizant Named Aston Martin Aramco Formula One™ ...
  url: https://www.prnewswire.com/news-releases/cognizant-named-aston-martin-aramco-formula-one-team-global-ai-services-partner-302755751.html
random_paper: 2
rate_limits:
- limit_count: 0
  name: Cognizant Technology Rate Limits
  slug: cognizant-technology-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 42.2
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 8.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cognizant-technology/refs/heads/main/screenshots/cognizant-technology-2026-06-20T174719.png
security:
- kind: authentication
  name: Cognizant Technology Authentication
  slug: cognizant-technology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cognizant Technology Domain Security
  slug: cognizant-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognizant Technology Vulnerability Disclosure
  slug: cognizant-technology-vulnerability-disclosure
  summary_line: Hackerone
slug: cognizant-technology
tags:
- AI Platform
- Consulting
- Digital Transformation
- IT Services
- Multi-Agent
- Neuro AI
- Fortune 500
website: https://www.cognizant.com/
---
