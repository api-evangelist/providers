---
aid: unix
url: https://raw.githubusercontent.com/api-evangelist/unix/refs/heads/main/apis.yml
apis:
- name: File System Operations API
  description: System calls for file and directory manipulation, including open, read, write, and file descriptor management.
  image: https://example.com/filesystem-icon.png
  humanUrl: https://man7.org/linux/man-pages/dir_section_2.html
  baseUrl: system://unix/fs
  tags:
  - Directories
  - Files
  - Filesystem
  - Io
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/contents.html
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man2/
  - type: Specification (Issue 8)
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html
  contact:
  - FN: POSIX Standards Committee
    email: standards@opengroup.org
  operations:
  - name: open
    description: Open file and return file descriptor
    parameters:
    - pathname
    - flags
    - mode
    returns: file descriptor (int)
  - name: read
    description: Read bytes from a file descriptor
    parameters:
    - fd
    - buf
    - count
    returns: number of bytes read
  - name: write
    description: Write bytes to a file descriptor
    parameters:
    - fd
    - buf
    - count
    returns: number of bytes written
  - name: close
    description: Close a file descriptor
    parameters:
    - fd
    returns: 0 on success, -1 on error
  - name: lseek
    description: Reposition file offset
    parameters:
    - fd
    - offset
    - whence
    returns: resulting offset
  - name: stat
    description: Get file status
    parameters:
    - pathname
    - statbuf
    returns: 0 on success, -1 on error
  - name: fstat
    description: Get file status by file descriptor
    parameters:
    - fd
    - statbuf
    returns: 0 on success, -1 on error
  - name: lstat
    description: Get file status without following symbolic links
    parameters:
    - pathname
    - statbuf
    returns: 0 on success, -1 on error
  - name: chmod
    description: Change file permissions
    parameters:
    - pathname
    - mode
    returns: 0 on success, -1 on error
  - name: fchmod
    description: Change file permissions by file descriptor
    parameters:
    - fd
    - mode
    returns: 0 on success, -1 on error
  - name: chown
    description: Change file owner and group
    parameters:
    - pathname
    - owner
    - group
    returns: 0 on success, -1 on error
  - name: mkdir
    description: Create a directory
    parameters:
    - pathname
    - mode
    returns: 0 on success, -1 on error
  - name: rmdir
    description: Remove a directory
    parameters:
    - pathname
    returns: 0 on success, -1 on error
  - name: link
    description: Create a hard link to a file
    parameters:
    - oldpath
    - newpath
    returns: 0 on success, -1 on error
  - name: unlink
    description: Delete a name and possibly the file it refers to
    parameters:
    - pathname
    returns: 0 on success, -1 on error
  - name: symlink
    description: Create a symbolic link
    parameters:
    - target
    - linkpath
    returns: 0 on success, -1 on error
  - name: readlink
    description: Read value of a symbolic link
    parameters:
    - pathname
    - buf
    - bufsiz
    returns: number of bytes placed in buf
  - name: rename
    description: Change the name or location of a file
    parameters:
    - oldpath
    - newpath
    returns: 0 on success, -1 on error
  - name: dup
    description: Duplicate a file descriptor
    parameters:
    - oldfd
    returns: new file descriptor
  - name: dup2
    description: Duplicate a file descriptor to a specified descriptor number
    parameters:
    - oldfd
    - newfd
    returns: new file descriptor
  - name: fcntl
    description: Manipulate file descriptor properties and flags
    parameters:
    - fd
    - cmd
    - arg
    returns: depends on cmd, -1 on error
  - name: access
    description: Check user permissions for a file
    parameters:
    - pathname
    - mode
    returns: 0 on success, -1 on error
  - name: umask
    description: Set file mode creation mask
    parameters:
    - mask
    returns: previous value of the mask
  - name: opendir
    description: Open a directory stream
    parameters:
    - name
    returns: pointer to directory stream
  - name: readdir
    description: Read a directory entry
    parameters:
    - dirp
    returns: pointer to dirent structure
  - name: closedir
    description: Close a directory stream
    parameters:
    - dirp
    returns: 0 on success, -1 on error
  - name: chdir
    description: Change working directory
    parameters:
    - path
    returns: 0 on success, -1 on error
  - name: getcwd
    description: Get current working directory
    parameters:
    - buf
    - size
    returns: pointer to buf
  - name: truncate
    description: Truncate a file to a specified length
    parameters:
    - path
    - length
    returns: 0 on success, -1 on error
  - name: ftruncate
    description: Truncate an open file to a specified length
    parameters:
    - fd
    - length
    returns: 0 on success, -1 on error
  - name: fsync
    description: Synchronize file state with storage device
    parameters:
    - fd
    returns: 0 on success, -1 on error
- name: Process Management API
  description: System calls for process creation, execution, termination, and control.
  image: https://example.com/process-icon.png
  humanUrl: https://man7.org/linux/man-pages/man2/fork.2.html
  baseUrl: system://unix/process
  tags:
  - Execution
  - Processes
  - Scheduling
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/fork.html
  - type: Tutorial
    url: https://sourceware.org/glibc/manual/
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  operations:
  - name: fork
    description: Create a new process by duplicating the calling process
    parameters: []
    returns: PID of child (in parent), 0 (in child), -1 on error
  - name: exec
    description: Execute a program (family of functions - execl, execv, execve, etc.)
    parameters:
    - pathname
    - argv
    - envp
    returns: does not return on success, -1 on error
  - name: wait
    description: Wait for process to change state
    parameters:
    - status
    returns: PID of terminated child
  - name: waitpid
    description: Wait for specific process to change state
    parameters:
    - pid
    - status
    - options
    returns: PID of child
  - name: exit
    description: Terminate the calling process
    parameters:
    - status
    returns: does not return
  - name: _exit
    description: Terminate the calling process immediately without cleanup
    parameters:
    - status
    returns: does not return
  - name: getpid
    description: Get process ID
    parameters: []
    returns: process ID
  - name: getppid
    description: Get parent process ID
    parameters: []
    returns: parent process ID
  - name: kill
    description: Send signal to a process
    parameters:
    - pid
    - sig
    returns: 0 on success, -1 on error
  - name: nice
    description: Change process priority
    parameters:
    - inc
    returns: new nice value
  - name: setpgid
    description: Set process group ID
    parameters:
    - pid
    - pgid
    returns: 0 on success, -1 on error
  - name: getpgid
    description: Get process group ID
    parameters:
    - pid
    returns: process group ID
  - name: setsid
    description: Create a new session and set process group ID
    parameters: []
    returns: session ID of new session
  - name: getrlimit
    description: Get resource limits for the process
    parameters:
    - resource
    - rlim
    returns: 0 on success, -1 on error
  - name: setrlimit
    description: Set resource limits for the process
    parameters:
    - resource
    - rlim
    returns: 0 on success, -1 on error
  - name: alarm
    description: Set an alarm clock for delivery of a signal
    parameters:
    - seconds
    returns: remaining seconds of previous alarm
  - name: pause
    description: Wait for a signal
    parameters: []
    returns: -1 with errno set to EINTR
  - name: posix_spawn
    description: Spawn a new process without fork (POSIX.1-2001)
    parameters:
    - pid
    - path
    - file_actions
    - attrp
    - argv
    - envp
    returns: 0 on success, error number on failure
- name: Interprocess Communication API
  description: System calls for communication between processes including pipes, signals, and shared memory.
  image: https://example.com/ipc-icon.png
  humanUrl: https://man7.org/linux/man-pages/man7/pipe.7.html
  baseUrl: system://unix/ipc
  tags:
  - Ipc
  - Pipes
  - Shared-Memory
  - Signals
  - Sockets
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html
  - type: Examples
    url: https://beej.us/guide/bgipc/
  - type: Network Programming Guide
    url: https://beej.us/guide/bgnet/html/
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man7/pipe.7.html
  operations:
  - name: pipe
    description: Create a pipe for interprocess communication
    parameters:
    - pipefd[2]
    returns: 0 on success, -1 on error
  - name: mkfifo
    description: Create a named pipe (FIFO special file)
    parameters:
    - pathname
    - mode
    returns: 0 on success, -1 on error
  - name: signal
    description: Install signal handler
    parameters:
    - signum
    - handler
    returns: previous signal handler
  - name: sigaction
    description: Examine and change signal action
    parameters:
    - signum
    - act
    - oldact
    returns: 0 on success, -1 on error
  - name: sigprocmask
    description: Examine and change blocked signals
    parameters:
    - how
    - set
    - oldset
    returns: 0 on success, -1 on error
  - name: sigpending
    description: Examine pending signals
    parameters:
    - set
    returns: 0 on success, -1 on error
  - name: sigsuspend
    description: Wait for a signal replacing the signal mask
    parameters:
    - mask
    returns: -1 with errno set to EINTR
  - name: socket
    description: Create an endpoint for communication
    parameters:
    - domain
    - type
    - protocol
    returns: file descriptor
  - name: bind
    description: Bind a name to a socket
    parameters:
    - sockfd
    - addr
    - addrlen
    returns: 0 on success, -1 on error
  - name: listen
    description: Listen for connections on a socket
    parameters:
    - sockfd
    - backlog
    returns: 0 on success, -1 on error
  - name: accept
    description: Accept a connection on a socket
    parameters:
    - sockfd
    - addr
    - addrlen
    returns: file descriptor
  - name: connect
    description: Initiate a connection on a socket
    parameters:
    - sockfd
    - addr
    - addrlen
    returns: 0 on success, -1 on error
  - name: send
    description: Send a message on a socket
    parameters:
    - sockfd
    - buf
    - len
    - flags
    returns: number of bytes sent
  - name: recv
    description: Receive a message from a socket
    parameters:
    - sockfd
    - buf
    - len
    - flags
    returns: number of bytes received
  - name: sendto
    description: Send a message on a socket to a specified address
    parameters:
    - sockfd
    - buf
    - len
    - flags
    - dest_addr
    - addrlen
    returns: number of bytes sent
  - name: recvfrom
    description: Receive a message from a socket with sender address
    parameters:
    - sockfd
    - buf
    - len
    - flags
    - src_addr
    - addrlen
    returns: number of bytes received
  - name: shutdown
    description: Shut down part of a full-duplex connection
    parameters:
    - sockfd
    - how
    returns: 0 on success, -1 on error
  - name: setsockopt
    description: Set options on a socket
    parameters:
    - sockfd
    - level
    - optname
    - optval
    - optlen
    returns: 0 on success, -1 on error
  - name: getsockopt
    description: Get options on a socket
    parameters:
    - sockfd
    - level
    - optname
    - optval
    - optlen
    returns: 0 on success, -1 on error
  - name: socketpair
    description: Create a pair of connected sockets
    parameters:
    - domain
    - type
    - protocol
    - sv[2]
    returns: 0 on success, -1 on error
  - name: shmget
    description: Allocate shared memory segment
    parameters:
    - key
    - size
    - shmflg
    returns: shared memory identifier
  - name: shmat
    description: Attach shared memory segment
    parameters:
    - shmid
    - shmaddr
    - shmflg
    returns: pointer to shared memory
  - name: shmdt
    description: Detach shared memory segment
    parameters:
    - shmaddr
    returns: 0 on success, -1 on error
  - name: shmctl
    description: Shared memory control operations
    parameters:
    - shmid
    - cmd
    - buf
    returns: depends on cmd, -1 on error
  - name: msgget
    description: Get a System V message queue identifier
    parameters:
    - key
    - msgflg
    returns: message queue identifier
  - name: msgsnd
    description: Send a message to a System V message queue
    parameters:
    - msqid
    - msgp
    - msgsz
    - msgflg
    returns: 0 on success, -1 on error
  - name: msgrcv
    description: Receive a message from a System V message queue
    parameters:
    - msqid
    - msgp
    - msgsz
    - msgtyp
    - msgflg
    returns: number of bytes copied into msgp
  - name: msgctl
    description: System V message queue control operations
    parameters:
    - msqid
    - cmd
    - buf
    returns: depends on cmd, -1 on error
- name: Memory Management API
  description: System calls for memory allocation, mapping, and protection.
  image: https://example.com/memory-icon.png
  humanUrl: https://man7.org/linux/man-pages/man2/mmap.2.html
  baseUrl: system://unix/memory
  tags:
  - Allocation
  - Memory
  - Mmap
  - Virtual-Memory
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/mmap.html
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man2/mmap.2.html
  operations:
  - name: brk
    description: Change data segment size
    parameters:
    - addr
    returns: 0 on success, -1 on error
  - name: sbrk
    description: Change data segment size
    parameters:
    - increment
    returns: previous program break
  - name: mmap
    description: Map files or devices into memory
    parameters:
    - addr
    - length
    - prot
    - flags
    - fd
    - offset
    returns: pointer to mapped area
  - name: munmap
    description: Unmap files or devices from memory
    parameters:
    - addr
    - length
    returns: 0 on success, -1 on error
  - name: mprotect
    description: Set protection on a region of memory
    parameters:
    - addr
    - len
    - prot
    returns: 0 on success, -1 on error
  - name: mlock
    description: Lock memory into RAM
    parameters:
    - addr
    - len
    returns: 0 on success, -1 on error
  - name: munlock
    description: Unlock memory from RAM
    parameters:
    - addr
    - len
    returns: 0 on success, -1 on error
  - name: msync
    description: Synchronize a memory-mapped file with its underlying storage
    parameters:
    - addr
    - length
    - flags
    returns: 0 on success, -1 on error
  - name: madvise
    description: Give advice about use of memory to the kernel
    parameters:
    - addr
    - length
    - advice
    returns: 0 on success, -1 on error
  - name: posix_memalign
    description: Allocate aligned memory
    parameters:
    - memptr
    - alignment
    - size
    returns: 0 on success, error number on failure
  - name: shm_open
    description: Create or open a POSIX shared memory object
    parameters:
    - name
    - oflag
    - mode
    returns: file descriptor
  - name: shm_unlink
    description: Remove a POSIX shared memory object
    parameters:
    - name
    returns: 0 on success, -1 on error
- name: System Information API
  description: System calls for retrieving system information and configuration.
  image: https://example.com/sysinfo-icon.png
  humanUrl: https://man7.org/linux/man-pages/man2/uname.2.html
  baseUrl: system://unix/sysinfo
  tags:
  - Configuration
  - Groups
  - Information
  - System
  - Users
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/uname.html
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man2/uname.2.html
  operations:
  - name: uname
    description: Get system information
    parameters:
    - buf
    returns: 0 on success, -1 on error
  - name: getuid
    description: Get user identity
    parameters: []
    returns: user ID
  - name: getgid
    description: Get group identity
    parameters: []
    returns: group ID
  - name: geteuid
    description: Get effective user ID
    parameters: []
    returns: effective user ID
  - name: getegid
    description: Get effective group ID
    parameters: []
    returns: effective group ID
  - name: setuid
    description: Set user identity
    parameters:
    - uid
    returns: 0 on success, -1 on error
  - name: setgid
    description: Set group identity
    parameters:
    - gid
    returns: 0 on success, -1 on error
  - name: seteuid
    description: Set effective user ID
    parameters:
    - euid
    returns: 0 on success, -1 on error
  - name: setegid
    description: Set effective group ID
    parameters:
    - egid
    returns: 0 on success, -1 on error
  - name: getgroups
    description: Get supplementary group IDs
    parameters:
    - size
    - list
    returns: number of supplementary group IDs
  - name: getlogin
    description: Get login name
    parameters: []
    returns: pointer to login name string
  - name: time
    description: Get time in seconds since Epoch
    parameters:
    - tloc
    returns: time value
  - name: gettimeofday
    description: Get time with microsecond precision
    parameters:
    - tv
    - tz
    returns: 0 on success, -1 on error
  - name: clock_gettime
    description: Get time from a specified clock with nanosecond precision
    parameters:
    - clockid
    - tp
    returns: 0 on success, -1 on error
  - name: clock_settime
    description: Set time for a specified clock
    parameters:
    - clockid
    - tp
    returns: 0 on success, -1 on error
  - name: sysconf
    description: Get configurable system variables at runtime
    parameters:
    - name
    returns: value of system variable, -1 on error
  - name: pathconf
    description: Get configurable pathname variables
    parameters:
    - path
    - name
    returns: value of variable, -1 on error
  - name: getenv
    description: Get value of an environment variable
    parameters:
    - name
    returns: pointer to value string, NULL if not found
  - name: setenv
    description: Set or change an environment variable
    parameters:
    - name
    - value
    - overwrite
    returns: 0 on success, -1 on error
  - name: gethostname
    description: Get the hostname of the system
    parameters:
    - name
    - len
    returns: 0 on success, -1 on error
- name: POSIX Threads API
  description: POSIX threads (pthreads) interface for creating and managing threads, mutexes, condition variables, and thread-specific data.
  image: https://example.com/threads-icon.png
  humanUrl: https://man7.org/linux/man-pages/man7/pthreads.7.html
  baseUrl: system://unix/pthreads
  tags:
  - Concurrency
  - Mutexes
  - Pthreads
  - Synchronization
  - Threads
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_create.html
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man7/pthreads.7.html
  - type: Header Reference
    url: https://man7.org/linux/man-pages/man0/pthread.h.0p.html
  - type: Specification (Issue 8)
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_create.html
  operations:
  - name: pthread_create
    description: Create a new thread
    parameters:
    - thread
    - attr
    - start_routine
    - arg
    returns: 0 on success, error number on failure
  - name: pthread_exit
    description: Terminate the calling thread
    parameters:
    - retval
    returns: does not return
  - name: pthread_join
    description: Wait for a thread to terminate
    parameters:
    - thread
    - retval
    returns: 0 on success, error number on failure
  - name: pthread_detach
    description: Detach a thread so its resources are freed on termination
    parameters:
    - thread
    returns: 0 on success, error number on failure
  - name: pthread_self
    description: Obtain ID of the calling thread
    parameters: []
    returns: thread ID
  - name: pthread_equal
    description: Compare two thread IDs
    parameters:
    - t1
    - t2
    returns: nonzero if equal, 0 if not equal
  - name: pthread_cancel
    description: Send a cancellation request to a thread
    parameters:
    - thread
    returns: 0 on success, error number on failure
  - name: pthread_mutex_init
    description: Initialize a mutex
    parameters:
    - mutex
    - attr
    returns: 0 on success, error number on failure
  - name: pthread_mutex_destroy
    description: Destroy a mutex
    parameters:
    - mutex
    returns: 0 on success, error number on failure
  - name: pthread_mutex_lock
    description: Lock a mutex
    parameters:
    - mutex
    returns: 0 on success, error number on failure
  - name: pthread_mutex_trylock
    description: Try to lock a mutex without blocking
    parameters:
    - mutex
    returns: 0 on success, error number on failure
  - name: pthread_mutex_unlock
    description: Unlock a mutex
    parameters:
    - mutex
    returns: 0 on success, error number on failure
  - name: pthread_cond_init
    description: Initialize a condition variable
    parameters:
    - cond
    - attr
    returns: 0 on success, error number on failure
  - name: pthread_cond_destroy
    description: Destroy a condition variable
    parameters:
    - cond
    returns: 0 on success, error number on failure
  - name: pthread_cond_wait
    description: Wait on a condition variable
    parameters:
    - cond
    - mutex
    returns: 0 on success, error number on failure
  - name: pthread_cond_signal
    description: Signal a condition variable waking one waiting thread
    parameters:
    - cond
    returns: 0 on success, error number on failure
  - name: pthread_cond_broadcast
    description: Broadcast a condition variable waking all waiting threads
    parameters:
    - cond
    returns: 0 on success, error number on failure
  - name: pthread_rwlock_init
    description: Initialize a read-write lock
    parameters:
    - rwlock
    - attr
    returns: 0 on success, error number on failure
  - name: pthread_rwlock_rdlock
    description: Lock a read-write lock for reading
    parameters:
    - rwlock
    returns: 0 on success, error number on failure
  - name: pthread_rwlock_wrlock
    description: Lock a read-write lock for writing
    parameters:
    - rwlock
    returns: 0 on success, error number on failure
  - name: pthread_rwlock_unlock
    description: Unlock a read-write lock
    parameters:
    - rwlock
    returns: 0 on success, error number on failure
  - name: pthread_key_create
    description: Create a thread-specific data key
    parameters:
    - key
    - destructor
    returns: 0 on success, error number on failure
  - name: pthread_setspecific
    description: Set thread-specific data value
    parameters:
    - key
    - value
    returns: 0 on success, error number on failure
  - name: pthread_getspecific
    description: Get thread-specific data value
    parameters:
    - key
    returns: pointer to thread-specific data, NULL if no value set
  - name: pthread_once
    description: Ensure initialization routine is called exactly once
    parameters:
    - once_control
    - init_routine
    returns: 0 on success, error number on failure
  - name: pthread_attr_init
    description: Initialize thread attributes object
    parameters:
    - attr
    returns: 0 on success, error number on failure
  - name: pthread_attr_destroy
    description: Destroy thread attributes object
    parameters:
    - attr
    returns: 0 on success, error number on failure
- name: I/O Multiplexing API
  description: System calls for monitoring multiple file descriptors for readiness, enabling event-driven and non-blocking I/O patterns.
  image: https://example.com/io-multiplex-icon.png
  humanUrl: https://man7.org/linux/man-pages/man2/select.2.html
  baseUrl: system://unix/io-multiplex
  tags:
  - Event-Driven
  - Io
  - Multiplexing
  - Non-Blocking
  - Poll
  - Select
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html
  - type: Man Pages
    url: https://man7.org/linux/man-pages/man2/select.2.html
  - type: Tutorial
    url: https://man7.org/linux/man-pages/man2/select_tut.2.html
  operations:
  - name: select
    description: Monitor multiple file descriptors for readiness using fd_set bitmasks
    parameters:
    - nfds
    - readfds
    - writefds
    - exceptfds
    - timeout
    returns: number of ready descriptors, 0 on timeout, -1 on error
  - name: pselect
    description: Synchronous I/O multiplexing with signal mask and timespec timeout
    parameters:
    - nfds
    - readfds
    - writefds
    - exceptfds
    - timeout
    - sigmask
    returns: number of ready descriptors, 0 on timeout, -1 on error
  - name: poll
    description: Monitor multiple file descriptors using pollfd array
    parameters:
    - fds
    - nfds
    - timeout
    returns: number of ready descriptors, 0 on timeout, -1 on error
  - name: ppoll
    description: Poll file descriptors with signal mask and timespec timeout
    parameters:
    - fds
    - nfds
    - tmo_p
    - sigmask
    returns: number of ready descriptors, 0 on timeout, -1 on error
- name: POSIX Semaphores API
  description: POSIX named and unnamed semaphore interfaces for process and thread synchronization.
  image: https://example.com/semaphore-icon.png
  humanUrl: https://man7.org/linux/man-pages/man7/sem_overview.7.html
  baseUrl: system://unix/semaphores
  tags:
  - Concurrency
  - Ipc
  - Semaphores
  - Synchronization
  properties:
  - type: Documentation
    url: https://man7.org/linux/man-pages/man7/sem_overview.7.html
  - type: Specification
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/sem_open.html
  operations:
  - name: sem_open
    description: Open or create a named semaphore
    parameters:
    - name
    - oflag
    - mode
    - value
    returns: pointer to semaphore, SEM_FAILED on error
  - name: sem_close
    description: Close a named semaphore
    parameters:
    - sem
    returns: 0 on success, -1 on error
  - name: sem_unlink
    description: Remove a named semaphore
    parameters:
    - name
    returns: 0 on success, -1 on error
  - name: sem_init
    description: Initialize an unnamed semaphore
    parameters:
    - sem
    - pshared
    - value
    returns: 0 on success, -1 on error
  - name: sem_destroy
    description: Destroy an unnamed semaphore
    parameters:
    - sem
    returns: 0 on success, -1 on error
  - name: sem_wait
    description: Lock (decrement) a semaphore, blocking if value is zero
    parameters:
    - sem
    returns: 0 on success, -1 on error
  - name: sem_trywait
    description: Try to lock a semaphore without blocking
    parameters:
    - sem
    returns: 0 on success, -1 on error
  - name: sem_timedwait
    description: Lock a semaphore with a timeout
    parameters:
    - sem
    - abs_timeout
    returns: 0 on success, -1 on error
  - name: sem_post
    description: Unlock (increment) a semaphore
    parameters:
    - sem
    returns: 0 on success, -1 on error
  - name: sem_getvalue
    description: Get the current value of a semaphore
    parameters:
    - sem
    - sval
    returns: 0 on success, -1 on error
- name: POSIX Message Queues API
  description: POSIX message queue interfaces for exchanging messages between processes with priority support.
  image: https://example.com/mq-icon.png
  humanUrl: https://man7.org/linux/man-pages/man7/mq_overview.7.html
  baseUrl: system://unix/mqueue
  tags:
  - Asynchronous
  - Ipc
  - Message-Queues
  - Messaging
  properties:
  - type: Documentation
    url: https://man7.org/linux/man-pages/man7/mq_overview.7.html
  - type: Specification
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/mq_open.html
  operations:
  - name: mq_open
    description: Open or create a POSIX message queue
    parameters:
    - name
    - oflag
    - mode
    - attr
    returns: message queue descriptor, (mqd_t)-1 on error
  - name: mq_close
    description: Close a message queue descriptor
    parameters:
    - mqdes
    returns: 0 on success, -1 on error
  - name: mq_unlink
    description: Remove a message queue
    parameters:
    - name
    returns: 0 on success, -1 on error
  - name: mq_send
    description: Send a message to a message queue
    parameters:
    - mqdes
    - msg_ptr
    - msg_len
    - msg_prio
    returns: 0 on success, -1 on error
  - name: mq_receive
    description: Receive a message from a message queue
    parameters:
    - mqdes
    - msg_ptr
    - msg_len
    - msg_prio
    returns: number of bytes received, -1 on error
  - name: mq_timedsend
    description: Send a message to a message queue with a timeout
    parameters:
    - mqdes
    - msg_ptr
    - msg_len
    - msg_prio
    - abs_timeout
    returns: 0 on success, -1 on error
  - name: mq_timedreceive
    description: Receive a message from a message queue with a timeout
    parameters:
    - mqdes
    - msg_ptr
    - msg_len
    - msg_prio
    - abs_timeout
    returns: number of bytes received, -1 on error
  - name: mq_notify
    description: Register for notification when a message is available
    parameters:
    - mqdes
    - sevp
    returns: 0 on success, -1 on error
  - name: mq_getattr
    description: Get message queue attributes
    parameters:
    - mqdes
    - attr
    returns: 0 on success, -1 on error
  - name: mq_setattr
    description: Set message queue attributes
    parameters:
    - mqdes
    - newattr
    - oldattr
    returns: 0 on success, -1 on error
- name: Terminal and Device I/O API
  description: POSIX terminal interface (termios) and device control system calls for managing terminals, serial ports, and device parameters.
  image: https://example.com/terminal-icon.png
  humanUrl: https://man7.org/linux/man-pages/man3/termios.3.html
  baseUrl: system://unix/terminal
  tags:
  - Device-Io
  - Serial
  - Terminal
  - Termios
  - Tty
  properties:
  - type: Documentation
    url: https://man7.org/linux/man-pages/man3/termios.3.html
  - type: Header Reference
    url: https://man7.org/linux/man-pages/man0/termios.h.0p.html
  - type: Specification
    url: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/termios.h.html
  operations:
  - name: tcgetattr
    description: Get terminal attributes
    parameters:
    - fd
    - termios_p
    returns: 0 on success, -1 on error
  - name: tcsetattr
    description: Set terminal attributes
    parameters:
    - fd
    - optional_actions
    - termios_p
    returns: 0 on success, -1 on error
  - name: tcsendbreak
    description: Send a break condition on a terminal
    parameters:
    - fd
    - duration
    returns: 0 on success, -1 on error
  - name: tcdrain
    description: Wait until all output has been transmitted
    parameters:
    - fd
    returns: 0 on success, -1 on error
  - name: tcflush
    description: Discard terminal data that has not been read or transmitted
    parameters:
    - fd
    - queue_selector
    returns: 0 on success, -1 on error
  - name: tcflow
    description: Suspend or restart transmission or reception of data
    parameters:
    - fd
    - action
    returns: 0 on success, -1 on error
  - name: cfgetispeed
    description: Get input baud rate from termios structure
    parameters:
    - termios_p
    returns: input baud rate
  - name: cfgetospeed
    description: Get output baud rate from termios structure
    parameters:
    - termios_p
    returns: output baud rate
  - name: cfsetispeed
    description: Set input baud rate in termios structure
    parameters:
    - termios_p
    - speed
    returns: 0 on success, -1 on error
  - name: cfsetospeed
    description: Set output baud rate in termios structure
    parameters:
    - termios_p
    - speed
    returns: 0 on success, -1 on error
  - name: isatty
    description: Test whether a file descriptor refers to a terminal
    parameters:
    - fd
    returns: 1 if terminal, 0 if not
  - name: ttyname
    description: Get the name of the terminal associated with a file descriptor
    parameters:
    - fd
    returns: pointer to terminal name string
  - name: ioctl
    description: Control device parameters and perform device-specific operations
    parameters:
    - fd
    - request
    - argp
    returns: depends on request, -1 on error
- name: File Locking API
  description: POSIX advisory file locking interfaces for coordinating file access between processes.
  image: https://example.com/lock-icon.png
  humanUrl: https://man7.org/linux/man-pages/man2/fcntl.2.html
  baseUrl: system://unix/file-locking
  tags:
  - Advisory-Locking
  - Concurrency
  - Fcntl
  - File-Locking
  properties:
  - type: Documentation
    url: https://man7.org/linux/man-pages/man2/fcntl.2.html
  - type: Specification
    url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/fcntl.html
  operations:
  - name: fcntl (F_SETLK)
    description: Set or release an advisory file lock without blocking
    parameters:
    - fd
    - F_SETLK
    - flock
    returns: 0 on success, -1 on error
  - name: fcntl (F_SETLKW)
    description: Set an advisory file lock, blocking if necessary
    parameters:
    - fd
    - F_SETLKW
    - flock
    returns: 0 on success, -1 on error
  - name: fcntl (F_GETLK)
    description: Test for the existence of a lock on a file region
    parameters:
    - fd
    - F_GETLK
    - flock
    returns: 0 on success, -1 on error
  - name: flock
    description: Apply or remove an advisory lock on an open file
    parameters:
    - fd
    - operation
    returns: 0 on success, -1 on error
  - name: lockf
    description: Apply, test, or remove a POSIX lock on an open file section
    parameters:
    - fd
    - cmd
    - len
    returns: 0 on success, -1 on error
name: UNIX System Call
tags:
- C-Api
- Ieee-1003
- Kernel
- Open-Group
- Operating-System
- Posix
- System-Calls
- Unix
type: Contract
image: https://example.com/unix-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Core UNIX/POSIX system calls providing low-level operating system interfaces for process management, file operations, interprocess communication, and system control.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

