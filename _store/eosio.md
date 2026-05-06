---
aid: eosio
url: https://raw.githubusercontent.com/api-evangelist/eosio/refs/heads/main/apis.yml
name: EOSIO
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Antelope
  - Blockchain
  - EOS
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-28'
position: Consumer
specificationVersion: '0.19'
description: EOSIO, now known as the Antelope protocol, is a free, open-source blockchain software protocol that provides developers and entrepreneurs with a platform on which to build, deploy, and run high-performing blockchain applications. Reference node software (nodeos) exposes HTTP/JSON RPC plugins for chain reads, history queries, transaction submission, and producer operations.
apis:
  - aid: eosio:nodeos-chain-api
    name: EOSIO Nodeos Chain API
    tags:
      - Antelope
      - Blockchain
      - Chain
      - JSON-RPC
    humanURL: https://github.com/AntelopeIO/leap
    properties:
      - url: openapi/eosio-nodeos-chain-api-openapi.yml
        type: OpenAPI
      - url: https://github.com/AntelopeIO/leap
        type: GitHubRepository
      - url: https://developers.eos.io/
        type: Documentation
    description: The chain_api_plugin in nodeos exposes JSON-RPC endpoints under /v1/chain for reading blockchain state, retrieving blocks and accounts, inspecting smart contract ABIs and tables, and submitting signed transactions to the network.
  - aid: eosio:nodeos-history-api
    name: EOSIO Nodeos History API
    tags:
      - Antelope
      - Blockchain
      - History
      - JSON-RPC
    humanURL: https://github.com/AntelopeIO/leap
    properties:
      - url: https://github.com/AntelopeIO/leap
        type: GitHubRepository
      - url: https://developers.eos.io/
        type: Documentation
    description: The history_api_plugin exposes endpoints under /v1/history for retrieving historical actions, transactions, key accounts, and controlled accounts. On modern Antelope deployments this is typically replaced by external history solutions like Hyperion or dfuse.
  - aid: eosio:nodeos-producer-api
    name: EOSIO Nodeos Producer API
    tags:
      - Antelope
      - Block Production
      - Blockchain
      - JSON-RPC
    humanURL: https://github.com/AntelopeIO/leap
    properties:
      - url: https://github.com/AntelopeIO/leap
        type: GitHubRepository
    description: The producer_api_plugin exposes endpoints under /v1/producer for controlling block production on a node, including pause, resume, schedule snapshots, and manage protocol features. Restricted to operators of block producing nodes.
  - aid: eosio:nodeos-net-api
    name: EOSIO Nodeos Net API
    tags:
      - Antelope
      - Blockchain
      - JSON-RPC
      - Networking
    humanURL: https://github.com/AntelopeIO/leap
    properties:
      - url: https://github.com/AntelopeIO/leap
        type: GitHubRepository
    description: The net_api_plugin exposes endpoints under /v1/net for inspecting and managing peer-to-peer connections of an Antelope node, including connections, status, connect, and disconnect operations.
common:
  - url: https://eosnetwork.com/
    name: EOS Network Foundation
    type: Website
  - url: https://developers.eos.io/
    name: Developer Portal
    type: Portal
  - url: https://developers.eos.io/welcome/latest/getting-started-guide/index
    name: Getting Started
    type: GettingStarted
  - url: https://developers.eos.io/welcome/latest/tutorials/index
    name: Tutorials
    type: Tutorials
  - url: https://developers.eos.io/welcome/latest/reference/index
    name: Documentation
    type: Documentation
  - url: https://developers.eos.io/welcome/latest/faq/index
    name: FAQ
    type: FAQ
  - url: https://github.com/AntelopeIO
    name: AntelopeIO GitHub Organization
    type: GitHub Organization
  - url: https://github.com/AntelopeIO/leap
    name: Leap (nodeos) GitHub Repository
    type: GitHubRepository
  - url: https://github.com/AntelopeIO/leap/releases
    name: Leap Releases
    type: Change Log
  - url: https://eos.io/legal/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://eos.io/legal/terms-of-use/
    name: Terms of Service
    type: TermsOfService
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
