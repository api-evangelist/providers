---
aid: international-business-machines
name: International Business Machines
description: IBM (International Business Machines) provides a comprehensive suite of cloud APIs spanning artificial intelligence, infrastructure, and data management. Key offerings include watsonx.ai for foundation model inference, watsonx Assistant for conversational AI, Natural Language Understanding and Speech services for text and audio processing, Cloud Object Storage for scalable data persistence, VPC infrastructure for virtual networking, and Kubernetes Service for container orchestration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Cloud
  - Enterprise
  - IBM
url: https://raw.githubusercontent.com/api-evangelist/international-business-machines/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: international-business-machines:watsonx-ai
    name: IBM Watsonx.ai API
    tags:
      - Artificial Intelligence
      - Machine Learning
      - Text Generation
    humanURL: https://cloud.ibm.com/apidocs/watsonx-ai
    properties:
      - url: https://cloud.ibm.com/apidocs/watsonx-ai
        type: Documentation
      - url: openapi/ibm-watsonx-ai-openapi.yml
        type: OpenAPI
      - url: json-schema/foundation-model.json
        type: JSONSchema
      - url: json-schema/text-generation-request.json
        type: JSONSchema
      - url: json-ld/international-business-machines-context.jsonld
        type: JSONLD
    description: The IBM watsonx.ai API enables developers to run text inference, prompt tuning, embeddings, and tokenization on Large Language Models. It provides access to multiple open source and IBM foundation models through a unified REST interface for building AI-powered applications.
  - aid: international-business-machines:watsonx-assistant
    name: IBM Watsonx Assistant V2 API
    tags:
      - Artificial Intelligence
      - Chatbots
      - Conversational AI
    humanURL: https://cloud.ibm.com/apidocs/assistant-v2
    properties:
      - url: https://cloud.ibm.com/apidocs/assistant-v2
        type: Documentation
      - url: openapi/ibm-watsonx-assistant-openapi.yml
        type: OpenAPI
      - url: json-schema/assistant-message.json
        type: JSONSchema
    description: The IBM watsonx Assistant v2 API enables developers to build conversational interfaces into applications, devices, and channels. It combines machine learning, natural language understanding, and an integrated dialog editor to create conversation flows between apps and users.
  - aid: international-business-machines:natural-language-understanding
    name: IBM Natural Language Understanding API
    tags:
      - Artificial Intelligence
      - Natural Language Processing
      - Text Analytics
    humanURL: https://cloud.ibm.com/apidocs/natural-language-understanding
    properties:
      - url: https://cloud.ibm.com/apidocs/natural-language-understanding
        type: Documentation
      - url: openapi/ibm-natural-language-understanding-openapi.yml
        type: OpenAPI
      - url: json-schema/nlu-analysis.json
        type: JSONSchema
    description: The IBM Natural Language Understanding API analyzes text content for sentiment, emotion, entities, keywords, categories, concepts, relations, and semantic roles. It processes plain text, HTML, or content from a public URL at scale using machine learning.
  - aid: international-business-machines:speech-to-text
    name: IBM Speech to Text API
    tags:
      - Artificial Intelligence
      - Audio
      - Speech Recognition
    humanURL: https://cloud.ibm.com/apidocs/speech-to-text
    properties:
      - url: https://cloud.ibm.com/apidocs/speech-to-text
        type: Documentation
      - url: openapi/ibm-speech-to-text-openapi.yml
        type: OpenAPI
      - url: json-schema/speech-recognition-result.json
        type: JSONSchema
    description: The IBM Speech to Text API provides speech-recognition capabilities to produce transcripts of spoken audio. It supports multiple languages and audio formats with features including speaker labels, keyword spotting, smart formatting, and custom language and acoustic models.
  - aid: international-business-machines:text-to-speech
    name: IBM Text to Speech API
    tags:
      - Artificial Intelligence
      - Audio
      - Speech Synthesis
    humanURL: https://cloud.ibm.com/apidocs/text-to-speech
    properties:
      - url: https://cloud.ibm.com/apidocs/text-to-speech
        type: Documentation
      - url: openapi/ibm-text-to-speech-openapi.yml
        type: OpenAPI
    description: The IBM Text to Speech API converts written text into natural-sounding speech in a variety of languages, dialects, and voices. It supports SSML input and multiple audio output formats for building voice-enabled applications.
  - aid: international-business-machines:cloud-object-storage
    name: IBM Cloud Object Storage API
    tags:
      - Cloud
      - Objects
      - Storage
    humanURL: https://cloud.ibm.com/docs/cloud-object-storage
    properties:
      - url: https://cloud.ibm.com/docs/cloud-object-storage
        type: Documentation
      - url: openapi/ibm-cloud-object-storage-openapi.yml
        type: OpenAPI
      - url: json-schema/bucket.json
        type: JSONSchema
    description: The IBM Cloud Object Storage API provides an S3-compatible RESTful interface for storing and retrieving objects in buckets. It supports multipart uploads, versioning, lifecycle policies, and server-side encryption for scalable unstructured data storage.
  - aid: international-business-machines:kubernetes-service
    name: IBM Cloud Kubernetes Service API
    tags:
      - Cloud
      - Containers
      - Kubernetes
    humanURL: https://cloud.ibm.com/apidocs/kubernetes/containers-v1-v2
    properties:
      - url: https://cloud.ibm.com/apidocs/kubernetes/containers-v1-v2
        type: Documentation
      - url: openapi/ibm-kubernetes-service-openapi.yml
        type: OpenAPI
      - url: json-schema/cluster.json
        type: JSONSchema
    description: The IBM Cloud Kubernetes Service API enables creation and management of Kubernetes and Red Hat OpenShift clusters on IBM Cloud. It supports provisioning clusters, managing worker nodes and pools, and integrating with IBM Cloud logging, monitoring, and security services.
  - aid: international-business-machines:vpc
    name: IBM Cloud VPC API
    tags:
      - Cloud
      - Infrastructure
      - Networking
    humanURL: https://cloud.ibm.com/apidocs/vpc/latest
    properties:
      - url: https://cloud.ibm.com/apidocs/vpc/latest
        type: Documentation
      - url: openapi/ibm-vpc-openapi.yml
        type: OpenAPI
      - url: json-schema/vpc.json
        type: JSONSchema
    description: The IBM Cloud VPC API enables programmatic provisioning and management of virtual server instances, networks, storage volumes, load balancers, security groups, and other infrastructure resources within an isolated virtual network on IBM Cloud.
common:
  - url: https://cloud.ibm.com/docs
    type: Documentation
  - url: https://developer.ibm.com/blogs/
    type: Blog
  - url: https://cloud.ibm.com/unifiedsupport/supportcenter
    type: Support
  - url: https://developer.ibm.com/apis/catalog
    type: Portal
  - url: https://github.com/IBM
    type: GitHub Organization
  - type: Features
    data:
      - 'International Business Machines (IBM): hundreds of services across Cloud + AI + Enterprise Software'
      - 'Detailed pricing: see https://www.ibm.com/cloud/pricing'
      - 'Service: See IBM Cloud catalog at cloud.ibm.com/catalog'
    sources:
      - https://www.ibm.com/cloud/pricing
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
