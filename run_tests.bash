fails=0
success=0
total=0
for test_script in $(ls tests); do
  total=$((total+1))
  success=$((success+1))

  bash tests/$test_script > /dev/null || {
    echo $test_script failed
    fails=$((fails+1))
    success=$((success-2))
  }
done


echo "Total Successes" $success
echo "Total Fails" $fails
echo "Total Tests" $total
