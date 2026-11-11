class DynamicArray {

    private int[] arr;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
        if (capacity <= 0) throw new IllegalArgumentException();
        this.arr      = new int[capacity];
        this.capacity = capacity;
        this.size     = 0;
    }

    /* ------------ core operations ------------ */

    public void pushback(int n) {
        ensureCapacity();          // 1) make room if full
        arr[size++] = n;           // 2) write at *size*, then bump size
    }

    public int popback() {
        if (size == 0) throw new IllegalStateException("array is empty");
        int n = arr[--size];       // 3) decrement first, then read
        arr[size] = 0;             // optional clear
        return n;
    }

    public int get(int i) {
        checkIndex(i);
        return arr[i];
    }

    /** Overwrite or append at the end. */
    public void set(int i, int n) {
        if (i < 0 || i > size) throw new IndexOutOfBoundsException();
        if (i == size) {           // appending
            ensureCapacity();
            size++;
        }
        arr[i] = n;
    }

    public int getSize()     { return size;     }
    public int getCapacity() { return capacity; }

    /* ------------ private helpers ------------ */

    private void ensureCapacity() {
        if (size == capacity) resize();
    }

    private void resize() {
        capacity *= 2;                             // update *both* …
        arr = java.util.Arrays.copyOf(arr, capacity);  // … the field and the array
    }

    private void checkIndex(int i) {
        if (i < 0 || i >= size) throw new IndexOutOfBoundsException();
    }
}
