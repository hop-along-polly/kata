package linkedList;

	public class DoubleLinkedList {
		
		Node head;
		Node tail;
		
//		Adds to the end of the the list
		public void add (Node node)
		{
			if (tail == null) {
				head = node;
				tail = node;
			}
			else
			{
				tail.next = node;
				node.previous = tail;
				tail = node;
			}
		}
		
		public boolean remove(int data)
		{
			if (tail == null) {
				return false;
			}
			Node current = head.next;
			while(current.next != null) {
				if(current.data == data) {
					current.next.previous = current.previous;
					current.previous.next = current.next;
					return true;
				}
				else {
					current = current.next;
				}
			}
			return false;
		}
		
		public boolean find(Node data) {
			if (tail == null) {
				return false;
			}
			else {
				
				return true;
			}
			
		}

}
