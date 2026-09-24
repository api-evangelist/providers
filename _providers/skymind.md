---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.pathmind.com
  baseurl_source: declared
  description: The Model Upload API from Pathmind — 1 operation(s) for model upload.
  name: Pathmind Model Upload API
  slug: skymind-model-upload-api
- baseURL: https://api.pathmind.com
  baseurl_source: declared
  description: The Projects API from Pathmind — 1 operation(s) for projects.
  name: Pathmind Projects API
  slug: skymind-projects-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pathmind Model Upload API
  slug: open-skymind-model-upload-api
- collection_type: open
  name: Pathmind Projects API
  slug: open-skymind-projects-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PathmindAI/pathmind-webapp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/PathmindAI/pathmind-webapp/releases
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/skills/skymind-upload-anylogic-model.md
  title: ''
  type: AgentSkill
  url: skills/skymind-upload-anylogic-model.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/overlays/skymind-pathmind-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/skymind-pathmind-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/PathmindAI/pathmind-webapp/blob/dev/LICENSE
- group: company
  title: ''
  type: Website
  url: https://pathmind.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PathmindAI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/PathmindAI/pathmind-webapp
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PathmindAI/pathmind-api/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/PathmindAI/pathmind-webapp/blob/dev/pathmind-api/src/main/resources/openapi.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/packages/skymind-packages.yml
  title: ''
  type: Packages
  url: packages/skymind-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/packages/skymind-packages.yml
  title: ''
  type: SDKs
  url: packages/skymind-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/well-known/skymind-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skymind-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/llms/skymind-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skymind-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/conformance/skymind-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skymind-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/lifecycle/skymind-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/skymind-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/changelog/skymind-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skymind-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/security/skymind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skymind-domain-security.yml
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/skymind_stock/
created: '2026-08-05'
description: 'Pathmind (formerly Skymind, the company behind the Deeplearning4j open-source deep learning library) was a San Francisco reinforcement-learning company that let simulation engineers train RL policies against AnyLogic and Python simulations without writing machine-learning code. The product had three parts: the Pathmind Helper, an AnyLogic palette item that exposed a simulation''s observations, actions and reward function to Pathmind; a cloud training service where uploaded models became experiments; and Pathmind Serving, a FastAPI/Ray policy server that turned a trained policy into a REST prediction endpoint. A small first-party REST API (project listing and AnyLogic model upload, authenticated with an X-PM-API-TOKEN header) and a first-party Python simulation API on PyPI were published. Pathmind ceased operating in November 2021 — its own final release, pathmind-webapp v1.8.6, is titled "Final release - disabling sign-ups and upgrades" — and the app, API and marketing hosts
  no longer serve. The artifacts in this repository are the surviving public first-party surface, harvested from the company''s own GitHub organization and PyPI.'
image: https://raw.githubusercontent.com/PathmindAI/pathmind-webapp/dev/pathmind-webapp/src/main/resources/static/frontend/images/pathmind-logo-100x100.png
layout: provider
modified: '2026-09-15'
name: Pathmind
nav: Providers
network: true
overview: 'Pathmind publishes 2 APIs on the [APIs.io](https://apis.io/) network: Model Upload API and Projects API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Reinforcement Learning, and Simulation.


  Pathmind''s developer surface includes documentation, API reference, changelog, and 16 more developer resources.'
random_paper: 19
screenshot: https://raw.githubusercontent.com/api-evangelist/skymind/refs/heads/main/screenshots/skymind-2026-09-02T155819.png
security:
- kind: authentication
  name: Skymind Authentication
  slug: skymind-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skymind Domain Security
  slug: skymind-domain-security
  summary_line: TLSv1.3
slug: skymind
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Reinforcement Learning
- Simulation
- Optimization
- Supply Chain
- Manufacturing
- Defunct
website: https://pathmind.com/
---
