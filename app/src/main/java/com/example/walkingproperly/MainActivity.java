package com.example.walkingproperly;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentStatePagerAdapter;
import androidx.viewpager.widget.ViewPager;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.tabs.TabLayout;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    ViewPager pager;
    TabLayout tab;
    ArrayList<Fragment> array;
    FloatingActionButton fab;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        pager = findViewById(R.id.pager);
        tab = findViewById(R.id.tab);

        //뷰페이저에 들어갈 프래그먼트를 프래그먼크 배열에 저장
        array = new ArrayList<>();
        array.add(new HomeFragment());
        array.add(new RecordFragment());
        array.add(new AnalyzeFragment());

        tab.addTab(tab.newTab()); //홈
        tab.addTab(tab.newTab()); //측정
        tab.addTab(tab.newTab()); //분석

        tab.getTabAt(0).setIcon(R.drawable.home);
        tab.getTabAt(1).setIcon(R.drawable.list);
        tab.getTabAt(2).setIcon(R.drawable.analyze);

        tab.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                pager.setCurrentItem(tab.getPosition());
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {

            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {

            }
        });

        //페이저 바뀌는 작업
        pager.addOnPageChangeListener(new TabLayout.TabLayoutOnPageChangeListener(tab));

        //페이저어댑터를 통해 프래그먼트 설정
        PagerAdapter ad = new PagerAdapter(getSupportFragmentManager());
        pager.setAdapter(ad);

        fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(MainActivity.this, "Nature", Toast.LENGTH_LONG).show();
            }
        });
    }

    //페이저어댑터 생성_프래그먼트어댑터
    class PagerAdapter extends FragmentStatePagerAdapter {

        public PagerAdapter(@NonNull FragmentManager fm) {
            super(fm);
        }

        @NonNull
        @Override
        public Fragment getItem(int position) {
            return array.get(position);
        }

        @Override
        public int getCount() {
            return array.size();
        }
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch(item.getItemId())
        {
            case R.id.addUser:
                Toast.makeText(MainActivity.this, "HI", Toast.LENGTH_LONG).show();
                break;
        }

        return super.onOptionsItemSelected(item);
    }
}