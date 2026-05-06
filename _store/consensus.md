---
aid: consensus
url: https://raw.githubusercontent.com/api-evangelist/consensus/refs/heads/main/apis.yml
name: Consensus
x-type: topic
description: Consensus is the distributed systems problem of getting a set of unreliable processes to agree on a value or sequence of values. Consensus algorithms power state-machine replication for databases, key-value stores, configuration systems, and blockchains. The consensus topic spans classical crash-fault tolerant algorithms (Paxos, Raft, Multi-Paxos, Zab, Viewstamped Replication) and Byzantine fault tolerant algorithms (PBFT, Tendermint, HotStuff, Casper FFG/CBC), and the impossibility result FLP that bounds what is possible in fully asynchronous models.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Algorithms
  - BFT
  - Blockchain
  - Consensus
  - Crash Fault Tolerance
  - Distributed Systems
  - Replication
  - State Machine
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: consensus:paxos
    name: Paxos
    description: Paxos is the classical crash-fault-tolerant consensus algorithm introduced by Leslie Lamport in 1989. Paxos and its derivatives (Multi-Paxos, Cheap Paxos, Vertical Paxos, EPaxos, Flexible Paxos) are foundational to distributed systems theory and are used in Google Chubby, Spanner, Megastore, and others.
    humanURL: https://lamport.azurewebsites.net/pubs/paxos-simple.pdf
    baseURL: https://lamport.azurewebsites.net
    tags:
      - Lamport
      - Paxos
      - Replication
    properties:
      - type: Specification
        url: https://lamport.azurewebsites.net/pubs/paxos-simple.pdf
      - type: Reference
        url: https://www.cs.utexas.edu/users/lorenzo/corsi/cs380d/papers/paper2-1.pdf
      - type: Reference
        url: https://en.wikipedia.org/wiki/Paxos_(computer_science)
    x-features:
      - Tolerates up to f crash failures with 2f+1 acceptors
      - Phases prepare, promise, accept, accepted
      - Multi-Paxos pipelines decisions for log replication
      - Underlies Google Chubby and Spanner
    x-useCases:
      - Replicated state machines
      - Distributed configuration services (Chubby, ZooKeeper-like)
      - Globally consistent databases
  - aid: consensus:raft
    name: Raft
    description: Raft is a consensus algorithm designed for understandability, published by Ongaro and Ousterhout in 2014. Raft separates leader election, log replication, and safety into distinct concepts and is implemented widely in etcd, Consul, CockroachDB, TiKV, MongoDB, and many other production systems.
    humanURL: https://raft.github.io/
    baseURL: https://raft.github.io
    tags:
      - etcd
      - Leader Election
      - Log Replication
      - Raft
    properties:
      - type: Specification
        url: https://raft.github.io/raft.pdf
      - type: Documentation
        url: https://raft.github.io/
      - type: Reference
        url: https://thesecretlivesofdata.com/raft/
    x-features:
      - Strong leader simplifies log replication
      - Randomized election timeouts
      - Membership changes via joint consensus
      - Snapshotting for log compaction
    x-useCases:
      - etcd, Consul, CockroachDB, TiKV, MongoDB replica sets
      - Replicated key-value stores
      - Configuration management for orchestrators
  - aid: consensus:pbft
    name: Practical Byzantine Fault Tolerance (PBFT)
    description: PBFT, by Castro and Liskov (1999), is a Byzantine fault-tolerant consensus protocol that tolerates up to f Byzantine failures with 3f+1 replicas. PBFT influenced subsequent BFT protocols including Tendermint and HotStuff.
    humanURL: http://pmg.csail.mit.edu/papers/osdi99.pdf
    baseURL: http://pmg.csail.mit.edu
    tags:
      - BFT
      - PBFT
    properties:
      - type: Specification
        url: http://pmg.csail.mit.edu/papers/osdi99.pdf
      - type: Reference
        url: https://en.wikipedia.org/wiki/Byzantine_fault
    x-features:
      - Tolerates Byzantine (arbitrary) failures
      - Three-phase commit protocol (pre-prepare, prepare, commit)
      - Foundation for many blockchain BFT consensus algorithms
    x-useCases:
      - Permissioned blockchains
      - Hardened configuration systems
      - Research baseline for new BFT protocols
  - aid: consensus:tendermint
    name: Tendermint / CometBFT
    description: Tendermint (now CometBFT) is a Byzantine fault-tolerant consensus engine that powers Cosmos SDK chains. CometBFT decouples consensus from application logic via the Application Blockchain Interface (ABCI), allowing custom blockchain applications in Go, Rust, and other languages.
    humanURL: https://docs.cometbft.com/
    baseURL: https://docs.cometbft.com
    tags:
      - ABCI
      - BFT
      - Blockchain
      - CometBFT
      - Cosmos
    properties:
      - type: Documentation
        url: https://docs.cometbft.com/
      - type: GitHubRepository
        url: https://github.com/cometbft/cometbft
      - type: Reference
        url: https://docs.cometbft.com/main/spec/consensus/consensus.html
    x-features:
      - Round-based BFT consensus with leader rotation
      - ABCI protocol decouples consensus from application
      - Instant finality on commit
      - Powers Cosmos Hub, Osmosis, and other Cosmos SDK chains
    x-useCases:
      - Building permissioned and permissionless blockchains
      - Custom application chains in the Cosmos ecosystem
  - aid: consensus:hotstuff
    name: HotStuff
    description: HotStuff is a leader-based BFT consensus protocol with linear view change and three-chain commit, designed by Yin et al. HotStuff is the foundation for Diem/Libra BFT and inspired modern protocols like Aptos AptosBFT and Sui's Mysticeti.
    humanURL: https://arxiv.org/abs/1803.05069
    baseURL: https://arxiv.org
    tags:
      - BFT
      - HotStuff
      - Linear
    properties:
      - type: Specification
        url: https://arxiv.org/abs/1803.05069
      - type: Reference
        url: https://github.com/hot-stuff/libhotstuff
      - type: Reference
        url: https://github.com/aptos-labs/aptos-core
    x-features:
      - Linear view change (O(n) message complexity)
      - Three-chain commit rule
      - Optimistic responsiveness
      - Foundation for Diem, Aptos, Sui consensus
    x-useCases:
      - Modern blockchain consensus designs
      - High-throughput, low-latency BFT systems
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Consensus_(computer_science)
  - type: Reference
    url: https://en.wikipedia.org/wiki/Paxos_(computer_science)
  - type: Reference
    url: https://en.wikipedia.org/wiki/Raft_(algorithm)
  - type: Reference
    url: https://en.wikipedia.org/wiki/Byzantine_fault
  - type: Reference
    url: https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf
  - type: Resources
    url: https://raft.github.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
