---
aid: vagrant
name: Vagrant
description: Vagrant, by HashiCorp, is a tool for building and managing virtualized development environments. Their developer platform provides APIs and SDKs for interacting with Vagrant Cloud and the HCP Vagrant Box Registry, enabling automation of box lifecycle management, plugin development, and integration with CI/CD pipelines.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - DevOps
  - Virtualization
  - Development Environments
  - Boxes
  - Cloud
  - HashiCorp
  - Infrastructure
created: '2026-03-20'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: vagrant:vagrant-cloud-api
    name: Vagrant Cloud API
    description: The Vagrant Cloud API v2 enables developers to programmatically interact with the Vagrant Cloud platform for managing Vagrant boxes, versions, and providers. It supports creating and updating boxes, publishing new versions, uploading provider binaries, and searching the public box catalog.
    humanURL: https://developer.hashicorp.com/vagrant/vagrant-cloud/api/v2
    baseURL: https://app.vagrantup.com/api/v2
    tags:
      - DevOps
      - Virtualization
      - Development Environments
      - Boxes
      - Cloud
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vagrant/vagrant-cloud/api/v2
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/openapi/vagrant-cloud-api-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/rules/vagrant-rules.yml
  - aid: vagrant:vagrant-hcp-box-registry
    name: HCP Vagrant Box Registry API
    description: The HCP Vagrant Box Registry API provides REST endpoints for managing Vagrant box registries and boxes on the HashiCorp Cloud Platform. The API uses HCP service principal credentials for authentication and is the successor to the legacy Vagrant Cloud service.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/vagrant-box-registry
    tags:
      - DevOps
      - Virtualization
      - Registry
      - Boxes
      - Cloud
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/vagrant-box-registry
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/openapi/vagrant-hcp-vagrant-box-registry-openapi.yml
  - aid: vagrant:vagrant-cloud-ruby-client
    name: Vagrant Cloud Ruby Client
    description: An official Ruby library that wraps the Vagrant Cloud API, providing a convenient interface for managing boxes, versions, and providers programmatically.
    humanURL: https://github.com/hashicorp/vagrant_cloud
    tags:
      - DevOps
      - Virtualization
      - SDK
      - Ruby
      - Boxes
    properties:
      - type: Documentation
        url: https://github.com/hashicorp/vagrant_cloud
      - type: SDK
        url: https://github.com/hashicorp/vagrant_cloud
  - aid: vagrant:vagrant-plugin-sdk
    name: Vagrant Plugin SDK
    description: The Vagrant Plugin SDK enables developers to build plugins that extend Vagrant with custom commands, providers, provisioners, guests, and host capabilities using Go or Ruby.
    humanURL: https://developer.hashicorp.com/vagrant/docs/plugins/development-basics
    tags:
      - DevOps
      - Virtualization
      - SDK
      - Plugins
      - Extensibility
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vagrant/docs/plugins/development-basics
common:
  - type: Portal
    url: https://developer.hashicorp.com/vagrant
  - type: Documentation
    url: https://developer.hashicorp.com/vagrant/docs
  - type: Website
    url: https://www.vagrantup.com/
  - type: PrivacyPolicy
    url: https://www.hashicorp.com/privacy
  - type: TermsOfService
    url: https://www.hashicorp.com/terms-of-service
  - type: Support
    url: https://support.hashicorp.com/
  - type: Blog
    url: https://www.hashicorp.com/blog
  - type: Login
    url: https://app.vagrantup.com/session/new
  - type: GitHub
    url: https://github.com/hashicorp/vagrant
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/json-schema/vagrant-box-schema.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/json-ld/vagrant-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/rules/vagrant-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/capabilities/box-lifecycle.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/vocabulary/vagrant-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
