package linkedList;

public class MyLinkedList {
	
	Node head;
	Node tail;
	
	public void add (Node node)
	{
		if (tail == null) {
			head = node;
			tail = node;
		}
		else
		{
			tail.next = node;
			tail = node;
		}
		
	}
	
	public void remove()
	{
		
	}
	
	public void find() {
		
	}
}	
