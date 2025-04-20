Map<String,List<Order>> ordersByCustomer = new HashMap<>();
for(Order o : orders){
    List<Order> list = ordersByCustomer.get(o.customerId);
    if(list==null){ list=new ArrayList<>(); }
    list.add(o);
    ordersByCustomer.put(o.customerId,list);
}
