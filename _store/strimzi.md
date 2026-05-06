---
aid: strimzi
name: Strimzi
description: Strimzi is a CNCF project providing a Kubernetes-native operator for running Apache Kafka on Kubernetes and OpenShift. It simplifies the deployment, management, scaling, and configuration of Kafka clusters using Kubernetes Custom Resource Definitions (CRDs). Strimzi manages the full Kafka ecosystem including brokers, ZooKeeper/KRaft, Kafka Connect, Kafka MirrorMaker 2, Kafka Bridge, and Schema Registry. The operator pattern lets teams declare desired Kafka topology via YAML manifests managed by Kubernetes.
url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/apis.yml
image: https://strimzi.io/images/logo/strimzi-logo.png
tags:
  - Kafka
  - Kubernetes
  - Messaging
  - Operator
  - Streaming
type: Index
access: 3rd-Party
position: Consumer
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: strimzi:strimzi-operator-api
    name: Strimzi Operator API
    description: The Strimzi Operator API is expressed through Kubernetes Custom Resource Definitions (CRDs). Operators are controlled by creating and modifying Kafka, KafkaTopic, KafkaUser, KafkaConnect, KafkaMirrorMaker2, KafkaBridge, and related custom resources via the Kubernetes API. The Strimzi operator watches these resources and reconciles the actual cluster state to match the desired specification.
    humanURL: https://strimzi.io/docs/operators/latest/configuring.html
    tags:
      - Kafka
      - Kubernetes
      - Messaging
      - Operator
      - Streaming
    properties:
      - type: Documentation
        url: https://strimzi.io/docs/operators/latest/
      - type: GitHub
        url: https://github.com/strimzi/strimzi-kafka-operator
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafka-crd.yml
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafkatopic-crd.yml
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafkauser-crd.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/json-schema/strimzi-kafka-schema.json
  - aid: strimzi:strimzi-kafka-bridge-api
    name: Strimzi Kafka Bridge REST API
    description: The Strimzi Kafka Bridge provides an HTTP/REST interface to Apache Kafka, allowing HTTP clients to produce and consume messages, manage consumer groups, and query topic metadata without a native Kafka client. The Bridge implements part of the OpenAPI specification for HTTP-to-Kafka bridging.
    humanURL: https://strimzi.io/docs/bridge/latest/
    baseURL: http://localhost:8080
    tags:
      - Kafka
      - Messaging
      - REST API
      - Streaming
    properties:
      - type: Documentation
        url: https://strimzi.io/docs/bridge/latest/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/openapi/strimzi-kafka-bridge-openapi.yml
      - type: GitHub
        url: https://github.com/strimzi/strimzi-kafka-bridge
common:
  - type: Website
    url: https://strimzi.io
  - type: Documentation
    url: https://strimzi.io/docs/operators/latest/
  - type: GitHub
    url: https://github.com/strimzi/strimzi-kafka-operator
  - type: Blog
    url: https://strimzi.io/blog/
  - type: Helm Chart
    url: https://artifacthub.io/packages/helm/strimzi/strimzi-kafka-operator
  - type: Slack
    url: https://slack.cncf.io
  - type: Changelog
    url: https://github.com/strimzi/strimzi-kafka-operator/releases
  - type: CNCF
    url: https://www.cncf.io/projects/strimzi/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/openapi/strimzi-kafka-bridge-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/json-schema/strimzi-kafka-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/json-ld/strimzi-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
