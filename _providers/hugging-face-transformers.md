---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 152
  human_in_the_loop: 2
  name: Hugging Face Transformers Agentic Access
  operation_count: 283
  slug: hugging-face-transformers-agentic-access
  summary_line: 283 operations · 152 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Open-source Python library that provides pretrained models, tokenizers, and pipelines for inference and fine-tuning across NLP, vision, audio, and multimodal tasks. The high-level pipeline API gives d
  name: Hugging Face Transformers Library
  slug: transformers-library
- description: Serverless inference API for running predictions against thousands of models hosted on the Hugging Face Hub. Supports NLP, computer vision, audio, and multimodal tasks through a unified HTTP interface
  name: Hugging Face Inference API
  slug: inference-api
- description: API for deploying and managing machine learning applications and demos using Gradio, Streamlit, or Docker on Hugging Face Spaces.
  name: Hugging Face Spaces API
  slug: spaces-api
- description: High-performance inference server for large language models with continuous batching, token streaming, tensor parallelism, and OpenAI-compatible chat completions endpoints.
  name: Text Generation Inference (TGI)
  slug: text-generation-inference
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints are for use with Agentic Provisioning Protocol.
  name: Hugging Face Transformers agentic-provisioning API
  slug: hugging-face-transformers-agentic-provisioning-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints get information about your currently used user based on the passed token.
  name: Hugging Face Transformers auth API
  slug: hugging-face-transformers-auth-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Git-free storage buckets for files, powered by Xet. Buckets provide simple file storage without git versioning.
  name: Hugging Face Transformers buckets API
  slug: hugging-face-transformers-buckets-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Use Collections to group repositories from the Hub (Models, Datasets, Spaces and Papers) on a dedicated page. You can learn more about it in the Collections [guide](https://huggingface.co/docs/hub/col
  name: Hugging Face Transformers collections API
  slug: hugging-face-transformers-collections-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Get information from all datasets on the Hub.
  name: Hugging Face Transformers datasets API
  slug: hugging-face-transformers-datasets-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints manage discussions.
  name: Hugging Face Transformers discussions API
  slug: hugging-face-transformers-discussions-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints are for interacting with the Hub's documentation.
  name: Hugging Face Transformers docs API
  slug: hugging-face-transformers-docs-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Manage inference endpoints.
  name: Hugging Face Transformers inference-endpoints API
  slug: hugging-face-transformers-inference-endpoints-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints manage jobs.
  name: Hugging Face Transformers jobs API
  slug: hugging-face-transformers-jobs-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Get information from all kernels on the Hub.
  name: Hugging Face Transformers kernels API
  slug: hugging-face-transformers-kernels-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Get information from all models on the Hub.
  name: Hugging Face Transformers models API
  slug: hugging-face-transformers-models-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints fetch Hub notifications.
  name: Hugging Face Transformers notifications API
  slug: hugging-face-transformers-notifications-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints are for use with OAuth.
  name: Hugging Face Transformers oauth API
  slug: hugging-face-transformers-oauth-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints let you interact with Hub Organizations and their members.
  name: Hugging Face Transformers orgs API
  slug: hugging-face-transformers-orgs-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoint gets information about papers.
  name: Hugging Face Transformers papers API
  slug: hugging-face-transformers-papers-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints help get information about models, datasets, and Spaces stored on the Hub.
  name: Hugging Face Transformers repo-search API
  slug: hugging-face-transformers-repo-search-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints manage repository settings like creating and deleting a repository.
  name: Hugging Face Transformers repos API
  slug: hugging-face-transformers-repos-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints manage resource groups. Resource groups are a Team or Enterprise feature.
  name: Hugging Face Transformers resource-groups API
  slug: hugging-face-transformers-resource-groups-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: 'Use the SCIM API to control and manage your hub Enterprise organization manage members'' access. ## Authentication - Must be organization owner - Use Access token with write permission on organization '
  name: Hugging Face Transformers scim API
  slug: hugging-face-transformers-scim-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Get information from all Spaces on the Hub.
  name: Hugging Face Transformers spaces API
  slug: hugging-face-transformers-spaces-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: Get information from SQL Console embeds from a dataset.
  name: Hugging Face Transformers sql-console API
  slug: hugging-face-transformers-sql-console-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: User accounts are the base authoring entity on the Hub
  name: Hugging Face Transformers users API
  slug: hugging-face-transformers-users-api
- baseURL: https://api-inference.huggingface.co
  baseurl_source: declared
  description: The following endpoints are for use with webhooks.
  name: Hugging Face Transformers webhooks API
  slug: hugging-face-transformers-webhooks-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hub API Endpoints agentic-provisioning API
  slug: open-hugging-face-transformers-agentic-provisioning-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning auth API
  slug: open-hugging-face-transformers-auth-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning buckets API
  slug: open-hugging-face-transformers-buckets-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning collections API
  slug: open-hugging-face-transformers-collections-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning datasets API
  slug: open-hugging-face-transformers-datasets-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning discussions API
  slug: open-hugging-face-transformers-discussions-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning docs API
  slug: open-hugging-face-transformers-docs-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning inference-endpoints API
  slug: open-hugging-face-transformers-inference-endpoints-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning jobs API
  slug: open-hugging-face-transformers-jobs-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning kernels API
  slug: open-hugging-face-transformers-kernels-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning models API
  slug: open-hugging-face-transformers-models-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning notifications API
  slug: open-hugging-face-transformers-notifications-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning oauth API
  slug: open-hugging-face-transformers-oauth-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning orgs API
  slug: open-hugging-face-transformers-orgs-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning papers API
  slug: open-hugging-face-transformers-papers-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning repo-search API
  slug: open-hugging-face-transformers-repo-search-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning repos API
  slug: open-hugging-face-transformers-repos-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning resource-groups API
  slug: open-hugging-face-transformers-resource-groups-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning scim API
  slug: open-hugging-face-transformers-scim-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning spaces API
  slug: open-hugging-face-transformers-spaces-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning sql-console API
  slug: open-hugging-face-transformers-sql-console-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning users API
  slug: open-hugging-face-transformers-users-api
- collection_type: open
  name: Hub API Endpoints agentic-provisioning webhooks API
  slug: open-hugging-face-transformers-webhooks-api
- collection_type: open
  name: Hub API Endpoints
  slug: open-hugging-face-transformers
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/huggingface/transformers/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/huggingface/transformers/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/huggingface/transformers/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/huggingface/transformers/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/huggingface/transformers/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hugging-face-transformers-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hugging-face-transformers-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hugging-face-transformers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hugging-face-transformers-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hugging-face-transformers-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/hugging-face-transformers-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hugging-face-transformers-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hugging-face-transformers-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hugging-face-transformers-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hugging-face-transformers-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hugging-face-transformers-hub-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/hugging-face-transformers-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hugging-face-transformers-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hugging-face-transformers-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hugging-face-transformers-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hugging-face-transformers-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/hugging-face-transformers-cli.yml
- group: design
  title: ''
  type: Components
  url: components/hugging-face-transformers-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hugging-face-transformers-data-model.yml
- group: company
  title: ''
  type: Website
  url: https://huggingface.co
- group: company
  title: ''
  type: Blog
  url: https://huggingface.co/blog
- group: docs
  title: ''
  type: Documentation
  url: https://huggingface.co/docs
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/hugging-face
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huggingface
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/huggingface
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huggingface
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/HuggingFace
- group: commercial
  title: ''
  type: TermsOfService
  url: https://huggingface.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://huggingface.co/privacy
- group: start
  title: ''
  type: Signup
  url: https://huggingface.co/join
- group: design
  title: ''
  type: Rules
  url: https://raw.githubusercontent.com/api-evangelist/hugging-face-transformers/refs/heads/main/hugging-face-transformers-rules.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/huggingface/transformers-to-mlx
created: '2024'
description: Hugging Face Transformers is an open-source machine learning library providing thousands of pretrained models and pipelines for Natural Language Processing, Computer Vision, Audio, and multimodal tasks. This index covers the Transformers library and the surrounding Hugging Face APIs that developers use to run inference, manage models, deploy demos, and serve LLMs at scale.
finops:
- name: Hugging Face Transformers Finops
  service_category: API
  slug: hugging-face-transformers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hugging-face-transformers.png
layout: provider
mcp_servers:
- description: ''
  name: Hugging Face Transformers MCP Server
  slug: hugging-face-transformers-mcp-server
modified: '2026-06-20'
name: Hugging Face Transformers
nav: Providers
network: true
overview: 'Hugging Face Transformers publishes 23 APIs on the [APIs.io](https://apis.io/) network, including agentic-provisioning API, auth API, buckets API, and 20 more. Tagged areas include Artificial Intelligence, Computer-Vision, Deep Learning, Machine-Learning, and Natural Language Processing.


  Hugging Face Transformers'' developer surface includes authentication, changelog, CLI, engineering blog, documentation, YouTube channel, signup flow, and 30 more developer resources.'
plans:
- name: Hugging Face Transformers Plans Pricing
  plan_count: 3
  slug: hugging-face-transformers-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Hugging Face Transformers Rate Limits
  slug: hugging-face-transformers-rate-limits
scopes:
- name: Hugging Face Transformers Scopes
  scope_count: 15
  slug: hugging-face-transformers-scopes
  summary_line: 15 scopes · authorizationCode/deviceCode
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hugging-face-transformers/refs/heads/main/screenshots/hugging-face-transformers-2026-06-20T182926.png
security:
- kind: authentication
  name: Hugging Face Transformers Authentication
  slug: hugging-face-transformers-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hugging Face Transformers Domain Security
  slug: hugging-face-transformers-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hugging Face Transformers Vulnerability Disclosure
  slug: hugging-face-transformers-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: transformers-to-mlx
  slug: transformers-to-mlx
slug: hugging-face-transformers
tags:
- Artificial Intelligence
- Computer-Vision
- Deep Learning
- Machine-Learning
- Natural Language Processing
- Open-Source
- Transformers
website: https://huggingface.co
---
