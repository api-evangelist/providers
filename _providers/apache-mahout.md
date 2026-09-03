---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Qumat is a unified Python API for building and executing quantum circuits across multiple quantum computing backends including Qiskit, Cirq, and Amazon Braket. It provides a hardware-agnostic interfac
  name: Qumat
  slug: qumat
- description: 'Mahout Samsara is a distributed linear algebra DSL in Scala for building machine learning algorithms on Apache Spark. It provides matrix decompositions, collaborative filtering, clustering, and other '
  name: Apache Mahout Samsara
  slug: apache-mahout-samsara
artifact_total: 23
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/mahout/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/mahout/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/mahout/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/mahout/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-mahout-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-mahout-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://mahout.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mahout
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/browse/MAHOUT
- group: other
  title: ''
  type: MailingList
  url: https://mahout.apache.org/docs/community/mailing-lists
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: company
  title: ''
  type: Blog
  url: https://mahout.apache.org/blog/atom.xml
created: '2026-03-16'
description: Apache Mahout is an open-source framework for building scalable machine learning applications. The project has evolved to include Qumat, a unified Python API for building quantum circuits that runs across multiple quantum backends including Qiskit, Cirq, and Amazon Braket, along with QDP for GPU-accelerated classical-to-quantum data encoding.
features:
- description: Qumat provides a unified API that runs the same quantum circuit code on Qiskit, Cirq, and Amazon Braket backends without modification.
  name: Hardware-Agnostic Quantum API
- description: Complete library of single-qubit gates (H, X, Y, Z, T, Rx, Ry, Rz, U) and multi-qubit gates (CNOT, Toffoli, SWAP, CSWAP).
  name: Quantum Gate Operations
- description: Support for symbolic parameters in rotation gates for variational quantum algorithms and quantum machine learning.
  name: Parameterized Quantum Circuits
- description: QDP provides zero-copy tensor transfer for encoding classical data into quantum states with GPU acceleration.
  name: GPU-Accelerated Data Encoding
- description: Samsara DSL enables large-scale matrix operations distributed across Apache Spark clusters.
  name: Distributed Linear Algebra
- description: Distributed recommendation algorithms including ALS-based collaborative filtering for large-scale datasets.
  name: Collaborative Filtering
- description: Distributed K-Means, fuzzy K-Means, and spectral clustering algorithms running on Spark.
  name: Clustering
- description: Distributed SVD, PCA, and random projection methods for large-scale feature reduction.
  name: Dimensionality Reduction
finops:
- name: Apache Mahout Finops
  service_category: API
  slug: apache-mahout-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-mahout.png
integrations:
- description: IBM Qiskit quantum computing framework as a Qumat execution backend for IBM quantum hardware and simulators.
  name: Qiskit
- description: Google Cirq quantum computing framework as a Qumat execution backend for Google quantum hardware.
  name: Cirq
- description: AWS Braket quantum computing service as a Qumat execution backend for cloud quantum hardware.
  name: Amazon Braket
- description: Primary distributed computing backend for Mahout Samsara linear algebra and machine learning algorithms.
  name: Apache Spark
layout: provider
modified: '2026-04-19'
name: Apache Mahout
nav: Providers
network: true
overview: 'Apache Mahout publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Distributed Computing, Machine-Learning, Python, Quantum Computing, and Scala.


  Apache Mahout''s developer surface includes developer portal, engineering blog, and 12 more developer resources.'
plans:
- name: Apache Mahout Plans Pricing
  plan_count: 3
  slug: apache-mahout-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Apache Mahout Rate Limits
  slug: apache-mahout-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 28.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-mahout/refs/heads/main/screenshots/apache-mahout-2026-06-20T172120.png
security:
- kind: domain-security
  name: Apache Mahout Domain Security
  slug: apache-mahout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Mahout Vulnerability Disclosure
  slug: apache-mahout-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-mahout
tags:
- Distributed Computing
- Machine-Learning
- Python
- Quantum Computing
- Scala
use_cases:
- description: Build variational quantum algorithms and quantum neural networks using parameterized circuits via the Qumat API.
  name: Quantum Machine Learning
- description: Prototype and test quantum algorithms across different hardware backends without rewriting circuit code.
  name: Quantum Algorithm Research
- description: Build distributed recommendation systems processing billions of user-item interactions using Mahout on Spark.
  name: Large-Scale Recommendation
- description: Cluster large datasets using distributed K-Means and other algorithms running on Apache Spark.
  name: Distributed Clustering
website: https://mahout.apache.org/
---
