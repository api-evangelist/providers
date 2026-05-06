---
aid: score
name: Score
description: Score is an open-source, platform-agnostic workload specification developed under the Cloud Native Computing Foundation (CNCF) Sandbox program. It provides a developer-centric YAML specification that enables teams to define application workloads once and deploy them across multiple container platforms including Docker Compose, Kubernetes, and cloud runtimes without environment-specific configuration drift. The score-spec organization provides reference CLI implementations (score-compose and score-k8s) that translate Score YAML into platform-specific manifests, eliminating YAML bloat and reducing cognitive load for platform engineering teams.
url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Platform Engineering
  - Cloud Native
  - CNCF
  - Workload Specification
  - Kubernetes
  - Docker
  - Developer Experience
  - Open Source
apis:
  - aid: score:score-specification
    name: Score Specification
    description: The Score Specification (score.yaml) is a declarative, platform-agnostic workload definition format that captures containers, service ports, and resource dependencies in a single file. Reference CLI implementations (score-compose and score-k8s) translate Score files into Docker Compose manifests or Kubernetes manifests respectively. The specification supports metadata, container definitions with environment variables and volume mounts, service port exposure, health probes, and resource references using placeholder syntax.
    humanURL: https://score.dev/
    tags:
      - Platform Engineering
      - Workload Specification
      - Cloud Native
      - CNCF
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.score.dev/
      - type: Specification
        url: https://docs.score.dev/docs/score-specification/score-spec-reference/
      - type: GitHub Repository
        url: https://github.com/score-spec/spec
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/vocabulary/score-vocabulary.yml
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/json-ld/score-context.jsonld
  - aid: score:score-compose
    name: score-compose
    description: score-compose is the reference Score implementation that translates Score YAML workload specifications into Docker Compose configuration files. It enables local development environments that mirror production workload definitions, supports resource provisioners for common dependencies like databases and message queues, and generates runnable Docker Compose files from a single score.yaml source.
    humanURL: https://score.dev/
    tags:
      - Docker Compose
      - CLI
      - Local Development
      - Platform Engineering
    properties:
      - type: Documentation
        url: https://docs.score.dev/docs/score-implementation/score-compose/
      - type: GitHub Repository
        url: https://github.com/score-spec/score-compose
  - aid: score:score-k8s
    name: score-k8s
    description: score-k8s is the reference Score implementation that translates Score YAML workload specifications into Kubernetes manifests including Deployments, Services, ConfigMaps, and Secrets. It supports Kubernetes resource provisioners, patch templates for customizing generated manifests, and enables consistent workload configuration from development to production on Kubernetes.
    humanURL: https://score.dev/
    tags:
      - Kubernetes
      - CLI
      - Platform Engineering
      - Cloud Native
    properties:
      - type: Documentation
        url: https://docs.score.dev/docs/score-implementation/score-k8s/
      - type: GitHub Repository
        url: https://github.com/score-spec/score-k8s
common:
  - type: Website
    url: https://score.dev/
  - type: GitHub Organization
    url: https://github.com/score-spec
  - type: Documentation
    url: https://docs.score.dev/
  - type: Slack Channel
    url: https://cloud-native.slack.com/archives/C07DN0D1UCW
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/json-ld/score-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/vocabulary/score-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
