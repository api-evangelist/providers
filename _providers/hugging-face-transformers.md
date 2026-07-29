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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 152
  human_in_the_loop: 2
  name: Hugging Face Transformers Agentic Access
  operation_count: 283
  slug: hugging-face-transformers-agentic-access
  summary_line: 283 operations · 152 acting · 2 human-in-the-loop
api_count: 27
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
- description: The following endpoints are for use with Agentic Provisioning Protocol.
  name: Hugging Face Transformers agentic-provisioning API
  slug: hugging-face-transformers-agentic-provisioning-api
- description: The following endpoints get information about your currently used user based on the passed token.
  name: Hugging Face Transformers auth API
  slug: hugging-face-transformers-auth-api
- description: Git-free storage buckets for files, powered by Xet. Buckets provide simple file storage without git versioning.
  name: Hugging Face Transformers buckets API
  slug: hugging-face-transformers-buckets-api
- description: Use Collections to group repositories from the Hub (Models, Datasets, Spaces and Papers) on a dedicated page. You can learn more about it in the Collections [guide](https://huggingface.co/docs/hub/col
  name: Hugging Face Transformers collections API
  slug: hugging-face-transformers-collections-api
- description: Get information from all datasets on the Hub.
  name: Hugging Face Transformers datasets API
  slug: hugging-face-transformers-datasets-api
- description: The following endpoints manage discussions.
  name: Hugging Face Transformers discussions API
  slug: hugging-face-transformers-discussions-api
- description: The following endpoints are for interacting with the Hub's documentation.
  name: Hugging Face Transformers docs API
  slug: hugging-face-transformers-docs-api
- description: Manage inference endpoints.
  name: Hugging Face Transformers inference-endpoints API
  slug: hugging-face-transformers-inference-endpoints-api
- description: The following endpoints manage jobs.
  name: Hugging Face Transformers jobs API
  slug: hugging-face-transformers-jobs-api
- description: Get information from all kernels on the Hub.
  name: Hugging Face Transformers kernels API
  slug: hugging-face-transformers-kernels-api
- description: Get information from all models on the Hub.
  name: Hugging Face Transformers models API
  slug: hugging-face-transformers-models-api
- description: The following endpoints fetch Hub notifications.
  name: Hugging Face Transformers notifications API
  slug: hugging-face-transformers-notifications-api
- description: The following endpoints are for use with OAuth.
  name: Hugging Face Transformers oauth API
  slug: hugging-face-transformers-oauth-api
- description: The following endpoints let you interact with Hub Organizations and their members.
  name: Hugging Face Transformers orgs API
  slug: hugging-face-transformers-orgs-api
- description: The following endpoint gets information about papers.
  name: Hugging Face Transformers papers API
  slug: hugging-face-transformers-papers-api
- description: The following endpoints help get information about models, datasets, and Spaces stored on the Hub.
  name: Hugging Face Transformers repo-search API
  slug: hugging-face-transformers-repo-search-api
- description: The following endpoints manage repository settings like creating and deleting a repository.
  name: Hugging Face Transformers repos API
  slug: hugging-face-transformers-repos-api
- description: The following endpoints manage resource groups. Resource groups are a Team or Enterprise feature.
  name: Hugging Face Transformers resource-groups API
  slug: hugging-face-transformers-resource-groups-api
- description: 'Use the SCIM API to control and manage your hub Enterprise organization manage members'' access. ## Authentication - Must be organization owner - Use Access token with write permission on organization '
  name: Hugging Face Transformers scim API
  slug: hugging-face-transformers-scim-api
- description: Get information from all Spaces on the Hub.
  name: Hugging Face Transformers spaces API
  slug: hugging-face-transformers-spaces-api
- description: Get information from SQL Console embeds from a dataset.
  name: Hugging Face Transformers sql-console API
  slug: hugging-face-transformers-sql-console-api
- description: User accounts are the base authoring entity on the Hub
  name: Hugging Face Transformers users API
  slug: hugging-face-transformers-users-api
- description: The following endpoints are for use with webhooks.
  name: Hugging Face Transformers webhooks API
  slug: hugging-face-transformers-webhooks-api
artifact_total: 38
collections:
- collection_type: open
  name: Hub API Endpoints
  slug: open-hugging-face-transformers
common:
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
  name: hugging-face-transformers-mcp.yml
  slug: hugging-face-transformers-mcpyml
modified: '2026-06-20'
name: Hugging Face Transformers
nav: Providers
network: true
overview: 'Hugging Face Transformers publishes 23 APIs on the [APIs.io](https://apis.io/) network, including agentic-provisioning API, auth API, buckets API, and 20 more. Tagged areas include Artificial Intelligence, Computer Vision, Deep Learning, Machine Learning, and Natural Language Processing.


  Hugging Face Transformers'' developer surface includes authentication, changelog, CLI, engineering blog, documentation, YouTube channel, signup flow, and 25 more developer resources.'
plans:
- name: Hugging Face Transformers Plans Pricing
  plan_count: 3
  slug: hugging-face-transformers-plans-pricing
random_paper: 24
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
  composite: 47.5
  delta: 1.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 45.8
    developer_ergonomics: 37.0
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Computer Vision
- Deep Learning
- Machine Learning
- Natural Language Processing
- Open Source
- Transformers
website: https://huggingface.co
---
