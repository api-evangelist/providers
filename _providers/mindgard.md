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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindgard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mindgard.ai
- group: other
  title: ''
  type: Platform
  url: https://mindgard.ai/platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindgard.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mindgard.ai/api-reference/projects/list-projects
- group: docs
  title: ''
  type: CLIReference
  url: https://docs.mindgard.ai/user-guide/cli-reference
- group: build
  title: ''
  type: PythonSDK
  url: https://docs.mindgard.ai/user-guide/python-sdk
- group: build
  title: ''
  type: AttackLibrary
  url: https://docs.mindgard.ai/attack-library/jailbreaks/overview
- group: build
  title: ''
  type: RemediationLibrary
  url: https://docs.mindgard.ai/remediation-library/anonymization-of-data
- group: design
  title: ''
  type: WorkflowIntegrations
  url: https://docs.mindgard.ai/user-guide/workflow-integrations
- group: other
  title: ''
  type: EnterpriseSetup
  url: https://docs.mindgard.ai/user-guide/enterprise-setup
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Mindgard
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/mindgard/
- group: build
  title: ''
  type: BurpExtension
  url: https://github.com/Mindgard/mindgard-burp-extension
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/Mindgard/mindgard-github-action-example
- group: other
  title: ''
  type: Research
  url: https://mindgard.ai/blog
- group: other
  title: ''
  type: Customers
  url: https://mindgard.ai/customers
- group: auth
  title: ''
  type: Disclosures
  url: https://mindgard.ai/disclosures
- group: other
  title: ''
  type: Services
  url: https://mindgard.ai/services
- group: learn
  title: ''
  type: AIAcademy
  url: https://mindgard.ai/ai-academy
- group: company
  title: ''
  type: Careers
  url: https://mindgard.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://mindgard.ai/contact
- group: company
  title: ''
  type: About
  url: https://mindgard.ai/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mindgard
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/mindgardai
- group: company
  title: ''
  type: Blog
  url: https://mindgard.ai/blog
created: '2026-05-25'
description: Mindgard is a UK-based offensive AI security company (London/Lancaster, spun out of Lancaster University) that provides an automated AI red-teaming and security testing platform for large language models, AI agents, and generative AI systems. Mindgard's platform combines AI Discovery and Recon (mapping the AI attack surface and shadow AI usage), continuous AI Red Teaming against evolving attacker techniques, AI Assessment, AI Runtime Protection, and Model Scanning, backed by a research-led attack library covering jailbreaks (ActorAttack, Crescendo, EvilConfidant, PersonGPT, DevModeV2, AsciiArtAttack, AntiGPT), prompt-injection techniques (Ascii85, AnsiEscaped, AnsiRaw and others), and policy/violation testing (MaliciousGeneration, PromptAlignment). Developers and security teams integrate Mindgard via a public REST API (projects, tests, multi-turn tests, datasets, findings, reconnaissance), a Python CLI (`pip install mindgard`), a Python SDK, a Burp Suite extension, and a GitHub
  Action for adding red-team checks to MLOps pipelines. The company also maintains and contributes to open-source security tooling including PyRIT integrations, an OpenAI-compatible LLM-Guard proxy, a chatbot API wrapper for testing web chatbots, and proof-of-concept vulnerability demonstrations (document RCE in LangChain agents, hidden audio jailbreaks, prompt-jailbreak demos). Mindgard's commercial model is enterprise SaaS with platform and services tiers; pricing is gated behind a sales conversation, and the platform is positioned for security, AppSec, and AI governance teams testing customer-facing or internally deployed AI systems.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindgard.png
layout: provider
modified: '2026-05-25'
name: Mindgard
nav: Providers
network: true
overview: 'Mindgard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Security, AI Red Teaming, LLM Security, Generative AI Security, and Prompt Injection.


  Mindgard''s developer surface includes documentation, API reference, GitHub presence, engineering blog, and 22 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindgard/refs/heads/main/screenshots/mindgard-2026-06-20T185600.png
security:
- kind: domain-security
  name: Mindgard Domain Security
  slug: mindgard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindgard
tags:
- AI Security
- AI Red Teaming
- LLM Security
- Generative AI Security
- Prompt Injection
- Jailbreak Testing
- AI Discovery
- AI Runtime Protection
- Model Scanning
- AI Governance
- Offensive Security
- MLOps
website: https://mindgard.ai
---
