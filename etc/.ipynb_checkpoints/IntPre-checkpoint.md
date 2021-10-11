### Kubernetes

### Networking
#### ARP, DNS, DHCP, TLS, Subnet, NAT, VLAN, IPv4 vs IPv6 and intercommunication
##### Subnet/CIDR : https://www.youtube.com/watch?v=OqsXzkXfwRw
##### NAT : https://www.youtube.com/watch?v=QBqPzHEDzvo
##### ARP, Switch, router : https://www.youtube.com/watch?v=rYodcvhh7b8
##### Routing + Switching : https://www.youtube.com/watch?v=Ep-x_6kggKA

### DSA

#### Cadane for product
#### Reverse linked list
#### Finding optimal available slot for booking hotel rooms (multiple rooms)
#### Dynamic programming example

### Design

#### Design patterns

### JPA

#### isolation levels
https://www.youtube.com/watch?v=4EajrPgJAk0
#### Optmistic locking, select for update
#### n+1 select
#### one-many, many-many etc mappings
#### inheritance strategy
#### merge, detach, re-attach
#### transaction, roll-back
#### transaction propagation

### Spring
#### AOP : point cut and advice
#### @Lazy
#### ApplicationContext scope

### Concurrency

#### Sample wait-notify impl
#### Linked blocking queue
#### Reentrant lock (only write lock)
#### Countdown latch
#### Producer-Consumer
#### Work stealing
#### ExecutorService internals
#### ForkJoinPool


### Java Collections:

#### HashMap internal working 
#### LinkedHashMap (Insterion order preserved) methods
#### TreeSet (R and B binary search tree) methods
#### PriorityQueue (heap) methods

https://www.baeldung.com/java-hashmap-load-factor   

When number of entries increase than loadFactor * capacity(or numberOfBuckets), number of buckets are increased and rehashing is done, which could be expensive in case of huge hashmaps, so better to choose the initial capacity wisely according to the usecase  

when entities in a bucket increase more than 8, balanced red-black tree is used instead of linkedList

#### Atomic Integer internal working

https://www.javacodemonk.com/what-is-atomicinteger-class-and-how-it-works-internally-1cda6a56  

It is non blocking, uses volatile and compare-and-swap hardware instruction  

class AtomicInteger {

    public final int getAndIncrement() {
        for (;;) {
            int current = get();
            int next = current + 1;
            if (compareAndSet(current, next))
                return current;
        }
    }
    //Rest of the implementation
}

##### General advice:
Use synchronized mechanism wherever thread contention is high i.e. multiple threads writes to the shared variable at the same point in time. Use AtomicInteger where thread contention is low to moderate to build highly scalable applications.

#### Deque : Double ended queue  
Elements can be added/retrieved/removed from both the ends, this can act as a FIFO queue as well as a LIFO stack   

#### ConcurrentHashMap



