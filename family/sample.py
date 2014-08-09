def maxi():
	n=raw_input('Enter :')
	n.split(",")
	a=max(n)
	return a

th>Attendance</th>


<div><input type="checkbox" name="attendance" value="attendance" checked></div>




<!-- function edit()
    {
        var street = document.getElementById('street');
        var city = document.getElementById('city');
        var code = document.getElementById('code');

    
            $.ajax({
               type: "POST",
               url: '/family/',
               data: {
                     post1:'post1',
                     csrfmiddlewaretoken: '{{csrf_token}}',
                      },
        
                success: function (response)
                    {
                    var data=response['data'];
                    var startstr = '';
                    for (i=0; i<data.length; i++)
                       // { 
                       // var street = data[i][0];
                       // var city = data[i][1];
                       // var code = data[i][2];
                       
                         
                       // }
                    };
                }
      
         
 -->


def cal():
  print "welcome to the application"
  print "select your option"
  choice = 0
  choice = input("Enter your option")
  if choice == 1:
      b = input("Enter")
      c = input("Enter")
      print b+c 
  elif choice == 2:
      b = input("Enter")
      c = input("Enter")
      print b-c 
  elif choice == 3:
      b = input("Enter")
      c = input("Enter")
      print b*c 
  elif choice == 4:
      b = input("Enter")
      c = input("Enter")
      print b/c 