{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"10aLz5ue4nMXVO6PRBEE9hdEAxYOgB21t","timestamp":1719415535565}],"authorship_tag":"ABX9TyOrR7cVyiWVuURjg9ZGhlIV"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["3+1\n","\n","3*3\n","\n","2**3\n","\n","\"Hello, world!\"  # only the last line is printed"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":36},"id":"b8bc41n2J9-C","executionInfo":{"status":"ok","timestamp":1719415662622,"user_tz":240,"elapsed":238,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"13306698-d735-4886-97e6-054bc1e3bec0"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["'Hello, world!'"],"application/vnd.google.colaboratory.intrinsic+json":{"type":"string"}},"metadata":{},"execution_count":4}]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"mOtEi0pv5UW4","executionInfo":{"status":"ok","timestamp":1719415575323,"user_tz":240,"elapsed":15,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"ecc92ea7-4d45-482c-bc37-e477fea23750"},"outputs":[{"output_type":"stream","name":"stdout","text":["4\n","9\n","8\n","Hello, world!\n"]}],"source":["print(3+1)\n","\n","print(3*3)\n","\n","print(2**3)\n","\n","print(\"Hello, world!\")       #print command does the trick for all the operations"]},{"cell_type":"markdown","source":["print([\"py\" + \"thon\"],[\"py\" * 3 + \"thon\"],[\"py\" - \"py\"],[\"3\" + 3], [3 * \"3\"], [a'], [a == 3], [a])\n"],"metadata":{"id":"tLy6mqP7G_Q_"}},{"cell_type":"code","source":["\"py\" * 3 + \"thon\""],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":36},"id":"00fzZSeMOoP7","executionInfo":{"status":"ok","timestamp":1719416824276,"user_tz":240,"elapsed":196,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"39f50029-c67f-4046-b51c-f848290281d4"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["'pypypython'"],"application/vnd.google.colaboratory.intrinsic+json":{"type":"string"}},"metadata":{},"execution_count":25}]},{"cell_type":"code","source":["print(\"py\" + \"thon\",\"py\" * 3 + \"thon\", [\"py\" + \"py\"],[3 * '3'],['a'], [ 'a' == 3], ['a'])\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"rKlpv_g-OE4V","executionInfo":{"status":"ok","timestamp":1719426321891,"user_tz":240,"elapsed":197,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"fb2b43f8-0a16-46ad-80c9-d8a35aae1397"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["python pypypython ['pypy'] ['333'] ['a'] [False] ['a']\n"]}]},{"cell_type":"code","source":["i= ((1 == 1), (1 == True), (0 == True), (0 == False), (3 == 1 * 3), ((3 == 1) * 3), ((3 == 3) * 4 + 3), (3**5 >= 4**4))\n","for j in i:\n","    print(j)\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"nDK-1OcSx_uy","executionInfo":{"status":"ok","timestamp":1719498237388,"user_tz":240,"elapsed":144,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"f7eb7a5c-3a34-4a05-895d-e8e90db35b6e"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["True\n","True\n","False\n","True\n","True\n","0\n","7\n","False\n"]}]},{"cell_type":"code","source":["i=((5/3), (5%3), (5.0/3), (5/3.0), (5.2%3))\n","for j in i:\n","    print(int(j))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ro54Y_KOO2dT","executionInfo":{"status":"ok","timestamp":1719501022237,"user_tz":240,"elapsed":118,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"4fe6a561-24ff-4078-a8c6-9d73e6fce01b"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["1\n","2\n","1\n","1\n","2\n"]}]},{"cell_type":"code","source":["i=((2000.3**200), (1.0 + 1.0 - 1.0), (1.0 + 1.0e20 - 1.0e20))  # 2000.3**200 (This operation results in a number\n","                                                               # that is too large to be represented as a\n","                                                               # standard floating-point number in Python, hence the overflow.)\n","for j in i:\n","    print(float(j))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":224},"id":"SdMNYOu0P2MC","executionInfo":{"status":"error","timestamp":1719804733843,"user_tz":300,"elapsed":357,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"4fb1a612-4cae-4b7d-a25e-16ef3a084c88"},"execution_count":22,"outputs":[{"output_type":"error","ename":"OverflowError","evalue":"(34, 'Numerical result out of range')","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mOverflowError\u001b[0m                             Traceback (most recent call last)","\u001b[0;32m<ipython-input-22-2f15d6e2cbc8>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mi\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2000.3\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0;36m200\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m1.0\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1.0\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1.0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m1.0\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1.0e20\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1.0e20\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# 2000.3**200 (This operation results in a number\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m                                                                \u001b[0;31m# that is too large to be represented as a\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m                                                                \u001b[0;31m# standard floating-point number in Python, hence the overflow.)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mOverflowError\u001b[0m: (34, 'Numerical result out of range')"]}]},{"cell_type":"code","source":["i=((1.0 + 1.0 - 1.0), (1.0 + 1.0e20 - 1.0e20))\n","for j in i:\n","    print(float(j))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"bnjfcqW-Qjzr","executionInfo":{"status":"ok","timestamp":1719501217566,"user_tz":240,"elapsed":163,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"b7085bf5-708c-4a93-dfb8-9cbd7ec62d3c"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["1.0\n","0.0\n"]}]},{"cell_type":"code","source":["x = 'Rishi'\n","print (f'hello, my name is {x}')"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Y4DAT9XOQl3C","executionInfo":{"status":"ok","timestamp":1719501486168,"user_tz":240,"elapsed":133,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"0dc08de1-2407-449e-bb1d-1fe6ea470582"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["hello, my name is Rishi\n"]}]},{"cell_type":"code","source":["i= (float(123), float('123'), float('123.23'), int(123), int('123'), int(float('123.23')), str(12), str(12.2), bool('a'), bool(0), bool(0.1))\n","for j in i:\n","    print(j)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"v_sNoQWjRjr1","executionInfo":{"status":"ok","timestamp":1719509340785,"user_tz":240,"elapsed":163,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"2672d90b-6f62-48c9-fb62-94842aa3ca98"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["123.0\n","123.0\n","123.23\n","123\n","123\n","123\n","12\n","12.2\n","True\n","False\n","True\n"]}]},{"cell_type":"code","source":["range(5)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"HitxieSywu-a","executionInfo":{"status":"ok","timestamp":1719509662189,"user_tz":240,"elapsed":171,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"61cc38d9-d61d-4ce5-da37-1c11b22f9eff"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["range(0, 5)"]},"metadata":{},"execution_count":16}]},{"cell_type":"code","source":["for i in range(5):\n","    print(i)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"AGt-r7icwzih","executionInfo":{"status":"ok","timestamp":1719509683054,"user_tz":240,"elapsed":153,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"328b78b0-77b9-4313-e706-9f8b4acf3dd2"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["0\n","1\n","2\n","3\n","4\n"]}]},{"cell_type":"code","source":["type(range(5))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Qk5YpqKZw4ok","executionInfo":{"status":"ok","timestamp":1719513602197,"user_tz":240,"elapsed":146,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"0f960d07-92f8-47ff-94ab-be52a9f7e2e7"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["range"]},"metadata":{},"execution_count":18}]},{"cell_type":"code","source":["for i in range(0,101):\n","    print(i)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ynDN--pI_1dS","executionInfo":{"status":"ok","timestamp":1719513728150,"user_tz":240,"elapsed":161,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"a5a429a2-ef6b-4a90-f5e3-312342704a04"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["0\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","11\n","12\n","13\n","14\n","15\n","16\n","17\n","18\n","19\n","20\n","21\n","22\n","23\n","24\n","25\n","26\n","27\n","28\n","29\n","30\n","31\n","32\n","33\n","34\n","35\n","36\n","37\n","38\n","39\n","40\n","41\n","42\n","43\n","44\n","45\n","46\n","47\n","48\n","49\n","50\n","51\n","52\n","53\n","54\n","55\n","56\n","57\n","58\n","59\n","60\n","61\n","62\n","63\n","64\n","65\n","66\n","67\n","68\n","69\n","70\n","71\n","72\n","73\n","74\n","75\n","76\n","77\n","78\n","79\n","80\n","81\n","82\n","83\n","84\n","85\n","86\n","87\n","88\n","89\n","90\n","91\n","92\n","93\n","94\n","95\n","96\n","97\n","98\n","99\n","100\n"]}]},{"cell_type":"code","source":["for i in range (0,101):\n","    if i % 7 == 0:\n","        print(i)\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Ba21y6GeABRz","executionInfo":{"status":"ok","timestamp":1719513845647,"user_tz":240,"elapsed":146,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"13f18566-a4f6-4f6a-a2ba-895c69677483"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["0\n","7\n","14\n","21\n","28\n","35\n","42\n","49\n","56\n","63\n","70\n","77\n","84\n","91\n","98\n"]}]},{"cell_type":"code","source":["for i in range(0,101,15):\n","   print(i)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"mdD3jRozBN8A","executionInfo":{"status":"ok","timestamp":1719514204834,"user_tz":240,"elapsed":131,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"943de3ed-54c3-4bda-fcf1-9ef3608b2a7c"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["0\n","15\n","30\n","45\n","60\n","75\n","90\n"]}]},{"cell_type":"code","source":["for i in range(0,101):\n","    if i % 5 == 0 and i % 3 !=0:\n","        print(i)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Zss-9DXOBtik","executionInfo":{"status":"ok","timestamp":1719796256618,"user_tz":300,"elapsed":567,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"73bb121f-6bdc-4a89-c048-044fddacb1ce"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["5\n","10\n","20\n","25\n","35\n","40\n","50\n","55\n","65\n","70\n","80\n","85\n","95\n","100\n"]}]},{"cell_type":"code","source":["x=5\n","\n","\n","if x == 2:\n","    print('prime number')\n","else:\n","    if x % 2 != 0:\n","        for i in range(1,x):\n","            if (i % 1 == 0 and i % x == 0):\n","                print(1,i)\n","    else:\n","          print('Not a prime')"],"metadata":{"id":"QxereROOEgZD"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["for x in range(2,21):\n","    for i in range(2,21):\n","        if x % i == 0:\n","            if x != i:\n","                print (i)\n","    print ('-------')"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"2-wgQKWJ1UDm","executionInfo":{"status":"ok","timestamp":1719796507319,"user_tz":300,"elapsed":781,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"outputId":"b9740af7-7402-41dd-9a58-10d9b5e6d18d"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["-------\n","-------\n","2\n","-------\n","-------\n","2\n","3\n","-------\n","-------\n","2\n","4\n","-------\n","3\n","-------\n","2\n","5\n","-------\n","-------\n","2\n","3\n","4\n","6\n","-------\n","-------\n","2\n","7\n","-------\n","3\n","5\n","-------\n","2\n","4\n","8\n","-------\n","-------\n","2\n","3\n","6\n","9\n","-------\n","-------\n","2\n","4\n","5\n","10\n","-------\n"]}]},{"cell_type":"code","source":["x = 4\n","if x <= 1:\n","  print('not a prime')\n","elif x == 2:\n","    print('PRIME')\n","elif x == 3:\n","    print('PRIME')\n","else:\n","  if x % 2 != 0 and x % 3 != 0:\n","    for i in range(4,x+1):\n","      if (i % 1 == 0 and x % i == 0):\n","        print(f'{x} is a PRIME NUMBER')\n","  else:\n","        print ('Not Prime')\n"],"metadata":{"id":"9YJiBV7C1U6K","executionInfo":{"status":"ok","timestamp":1719804716797,"user_tz":300,"elapsed":216,"user":{"displayName":"Rishi C","userId":"00417959617401892635"}},"colab":{"base_uri":"https://localhost:8080/"},"outputId":"010b743f-b98b-471d-96eb-2f904fab044f"},"execution_count":21,"outputs":[{"output_type":"stream","name":"stdout","text":["Not Prime\n"]}]},{"cell_type":"code","source":[],"metadata":{"id":"4q3OLbse1cgY"},"execution_count":null,"outputs":[]}]}