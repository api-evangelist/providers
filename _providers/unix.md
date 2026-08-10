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
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: System calls for file and directory manipulation, including open, read, write, and file descriptor management.
  name: File System Operations API
  slug: file-system-operations-api
- description: System calls for process creation, execution, termination, and control.
  name: Process Management API
  slug: process-management-api
- description: System calls for communication between processes including pipes, signals, and shared memory.
  name: Interprocess Communication API
  slug: interprocess-communication-api
- description: System calls for memory allocation, mapping, and protection.
  name: Memory Management API
  slug: memory-management-api
- description: System calls for retrieving system information and configuration.
  name: System Information API
  slug: system-information-api
- description: POSIX threads (pthreads) interface for creating and managing threads, mutexes, condition variables, and thread-specific data.
  name: POSIX Threads API
  slug: posix-threads-api
- description: System calls for monitoring multiple file descriptors for readiness, enabling event-driven and non-blocking I/O patterns.
  name: I/O Multiplexing API
  slug: io-multiplexing-api
- description: POSIX named and unnamed semaphore interfaces for process and thread synchronization.
  name: POSIX Semaphores API
  slug: posix-semaphores-api
- description: POSIX message queue interfaces for exchanging messages between processes with priority support.
  name: POSIX Message Queues API
  slug: posix-message-queues-api
- description: POSIX terminal interface (termios) and device control system calls for managing terminals, serial ports, and device parameters.
  name: Terminal and Device I/O API
  slug: terminal-and-device-io-api
- description: POSIX advisory file locking interfaces for coordinating file access between processes.
  name: File Locking API
  slug: file-locking-api
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unix-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://pubs.opengroup.org/onlinepubs/9799919799/
- group: docs
  title: ''
  type: Documentation
  url: https://pubs.opengroup.org/onlinepubs/9699919799/
- group: docs
  title: ''
  type: Documentation
  url: https://man7.org/linux/man-pages/dir_section_2.html
- group: start
  title: ''
  type: GettingStarted
  url: https://sourceware.org/glibc/manual/
- group: other
  title: ''
  type: Resources
  url: https://en.wikipedia.org/wiki/POSIX
- group: docs
  title: ''
  type: APIReference
  url: https://unix.org/apis.html
- group: docs
  title: ''
  type: Documentation
  url: https://standards.ieee.org/ieee/1003.1/7700/
created: '2024-01-15'
description: Core UNIX/POSIX system calls providing low-level operating system interfaces for process management, file operations, interprocess communication, and system control.
features:
- File system operations and file descriptor management
- Process creation, execution, and control
- Interprocess communication via pipes, signals, and sockets
- Memory mapping and virtual memory management
- POSIX threads for concurrent programming
- I/O multiplexing with select and poll
- Named and unnamed semaphores
- Message queues for async process communication
- Terminal and device I/O control
- Advisory file locking
finops:
- name: Unix Finops
  service_category: API
  slug: unix-finops
image: /assets/icons/unix.png
integrations:
- Linux kernel
- macOS / Darwin
- FreeBSD
- GNU C Library (glibc)
- musl libc
- POSIX-compliant operating systems
layout: provider
modified: '2026-04-18'
name: UNIX System Call
nav: Providers
network: true
overview: 'UNIX System Call publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include C-Api, Ieee-1003, Kernel, Open-Group, and Operating-System.


  UNIX System Call''s developer surface includes documentation, getting-started guide, API reference, and 5 more developer resources.'
plans:
- name: Unix Plans Pricing
  plan_count: 3
  slug: unix-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 5
  name: Unix Rate Limits
  slug: unix-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unix/refs/heads/main/screenshots/unix-2026-06-20T200339.png
security:
- kind: domain-security
  name: Unix Domain Security
  slug: unix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unix
tags:
- C-Api
- Ieee-1003
- Kernel
- Open-Group
- Operating-System
- Posix
- System-Calls
- Unix
use_cases:
- Operating system development
- Systems programming and embedded systems
- Network server and daemon development
- High-performance I/O applications
- Concurrent and multi-threaded programming
- Device driver and hardware interface development
---
