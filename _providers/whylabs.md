---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: whylogs is an open-source data logging library that creates approximate statistical profiles of datasets, enabling drift detection, data quality monitoring, and bias analysis for ML pipelines. Support
  name: whylogs
  slug: whylogs
- description: LangKit is an open-source toolkit that extracts telemetry from LLM prompts and responses including relevance, sentiment, toxicity, prompt injection signals, jailbreak similarity, refusal patterns, and
  name: LangKit
  slug: langkit
- description: 'WhyLabs Observability is the historical commercial SaaS that ingested whylogs profiles and LangKit telemetry for dashboards, drift alerts, and constraint monitoring. WhyLabs, Inc. has announced it is '
  name: WhyLabs Observability Platform
  slug: whylabs-observability
artifact_total: 23
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/whylabs/whylogs/blob/mainline/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whylabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whylabs.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whylabs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/whylabs/whylogs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/whylabs/langkit
- group: docs
  title: ''
  type: WhylogsDocumentation
  url: https://whylogs.readthedocs.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whylabs/
- group: operate
  title: ''
  type: CompanyStatus
  url: https://whylabs.ai/
created: '2026-05-23'
description: WhyLabs was an AI observability platform focused on data and model monitoring for both classical ML and LLM workloads. It built and maintained whylogs, an open-source data logging library that produces statistical profiles of tabular and unstructured data, and LangKit, an open-source toolkit for LLM telemetry covering relevance, toxicity, prompt injection signals, and quality metrics. WhyLabs, Inc. has announced it is discontinuing operations and has open-sourced its platform; the whylogs and LangKit projects remain available on GitHub for community use and research.
features:
- description: Privacy-preserving statistical profiles of tabular, text, image, and embedding data.
  name: whylogs Profiling
- description: Out-of-the-box metrics for relevance, toxicity, prompt injection signals, and refusal patterns.
  name: LangKit LLM Telemetry
- description: Compare profiles over time to detect data and concept drift.
  name: Drift Detection
- description: Constraint-based checks on schema, ranges, missingness, and distribution properties.
  name: Data Quality Monitoring
- description: Profile-driven analysis of model inputs and outputs across protected groups.
  name: Bias and Fairness Analysis
- description: Core libraries remain available under permissive licenses on GitHub.
  name: Open Source
finops:
- name: Whylabs Finops
  service_category: API
  slug: whylabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whylabs.png
integrations:
- description: Profile pandas DataFrames directly with whylogs.
  name: pandas
- description: Generate whylogs profiles from PySpark and Spark Scala jobs.
  name: Spark
- description: Profile Snowflake tables for drift and quality monitoring.
  name: Snowflake
- description: Read and write whylogs profiles to S3 for distributed pipelines.
  name: AWS S3
- description: Log whylogs profiles alongside MLflow runs and models.
  name: MLflow
- description: Apply LangKit metrics to Hugging Face model outputs.
  name: Hugging Face
layout: provider
modified: '2026-05-23'
name: WhyLabs
nav: Providers
network: true
overview: WhyLabs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Observability, ML Monitoring, LLM Monitoring, Open Source, and whylogs.
plans:
- name: Whylabs Plans Pricing
  plan_count: 1
  slug: whylabs-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Whylabs Rate Limits
  slug: whylabs-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whylabs/refs/heads/main/screenshots/whylabs-2026-06-20T201448.png
security:
- kind: domain-security
  name: Whylabs Domain Security
  slug: whylabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: whylabs
tags:
- AI Observability
- ML Monitoring
- LLM Monitoring
- Open Source
- whylogs
- LangKit
- Discontinued
use_cases:
- description: Monitor training and inference datasets for schema drift and quality issues.
  name: ML Data Quality
- description: Instrument LLM applications with LangKit metrics to track safety and quality over time.
  name: LLM Telemetry
- description: Detect distribution shifts in features and predictions for production ML models.
  name: Model Drift Monitoring
- description: Share statistical profiles between teams and environments without exposing raw data.
  name: Privacy-Preserving Logging
website: https://whylabs.ai/
---
